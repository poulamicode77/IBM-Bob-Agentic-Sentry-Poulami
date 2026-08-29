"""
test_modern_app.py — pytest suite for modern_app.py

Run:
    pip install fastapi[all] pytest httpx
    pytest test_modern_app.py -v
"""
import sqlite3
import os
import pytest
from fastapi.testclient import TestClient

# Point the app at an isolated in-memory database for every test run
os.environ["DATABASE_URL"] = ":memory:"
os.environ["API_KEY"] = ""  # disable auth for most tests; overridden per test

import modern_app  # noqa: E402  (must come after env vars are set)
from modern_app import app, DATABASE_URL  # noqa: E402

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def _seed_db(monkeypatch, tmp_path):
    """
    Create a fresh on-disk SQLite DB per test, seed one user, and patch the
    module-level DATABASE_URL so every get_db() call uses this file.
    """
    db_file = str(tmp_path / "test_users.db")
    conn = sqlite3.connect(db_file)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email    TEXT NOT NULL
        )
        """
    )
    conn.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        ("alice", "alice@example.com"),
    )
    conn.commit()
    conn.close()

    monkeypatch.setattr(modern_app, "DATABASE_URL", db_file)


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def client_with_auth(monkeypatch):
    """Client that sends the correct API key (auth enabled)."""
    monkeypatch.setattr(modern_app, "API_KEY", "test-secret")
    c = TestClient(app)
    c.headers.update({"X-API-Key": "test-secret"})
    return c

# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# ---------------------------------------------------------------------------
# Successful retrieval — 200 OK
# ---------------------------------------------------------------------------

def test_get_existing_user_returns_200(client):
    """Seeded user id=1 must be retrievable."""
    response = client.get("/api/v2/users/1")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["username"] == "alice"
    assert body["email"] == "alice@example.com"

# ---------------------------------------------------------------------------
# User not found — 404 Not Found
# ---------------------------------------------------------------------------

def test_get_nonexistent_user_returns_404(client):
    """A user id that has never been inserted must yield 404."""
    response = client.get("/api/v2/users/9999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

# ---------------------------------------------------------------------------
# SQL Injection resilience
# ---------------------------------------------------------------------------

def test_sql_injection_in_path_rejected_as_unprocessable(client):
    """
    Classic SQL-injection payload in the path segment.
    FastAPI validates user_id as `int`; a non-integer string must produce
    422 Unprocessable Entity — the payload never reaches the database.
    """
    malicious = "1' OR '1'='1"
    response = client.get(f"/api/v2/users/{malicious}")
    assert response.status_code == 422  # type coercion failure, not a DB hit


def test_sql_injection_large_numeric_string_not_found(client):
    """
    Even if the attacker supplies a numeric-looking payload that passes type
    validation, no extra rows are returned — parameterised query isolates it.
    """
    response = client.get("/api/v2/users/999999999")
    assert response.status_code == 404

# ---------------------------------------------------------------------------
# Invalid / missing parameter validation — 422 Unprocessable Entity
# ---------------------------------------------------------------------------

def test_non_integer_user_id_returns_422(client):
    """Alphabetic user_id must be rejected by FastAPI before hitting the DB."""
    response = client.get("/api/v2/users/abc")
    assert response.status_code == 422


def test_float_user_id_returns_422(client):
    """Floating-point user_id must also be rejected."""
    response = client.get("/api/v2/users/1.5")
    assert response.status_code == 422

# ---------------------------------------------------------------------------
# Authentication — 401 when API key is required but missing / wrong
# ---------------------------------------------------------------------------

def test_missing_api_key_returns_401(monkeypatch):
    """When API_KEY is set, a request without the header must be rejected."""
    monkeypatch.setattr(modern_app, "API_KEY", "required-secret")
    c = TestClient(app)
    response = c.get("/api/v2/users/1")
    assert response.status_code == 401


def test_wrong_api_key_returns_401(monkeypatch):
    """Wrong key value must also yield 401."""
    monkeypatch.setattr(modern_app, "API_KEY", "required-secret")
    c = TestClient(app)
    response = c.get("/api/v2/users/1", headers={"X-API-Key": "wrong-key"})
    assert response.status_code == 401


def test_correct_api_key_succeeds(client_with_auth):
    """Correct key must allow the request through."""
    response = client_with_auth.get("/api/v2/users/1")
    assert response.status_code == 200
