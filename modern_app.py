"""
modern_app.py — FastAPI microservice (modernised from legacy_app.py)

Improvements over legacy:
  - Secrets loaded from environment variables (no hardcoded values)
  - Parameterised SQL queries (no injection surface)
  - Pydantic models for strict request / response validation
  - Proper HTTP status codes and structured error responses
  - /health endpoint for liveness checks
"""
import os
import sqlite3
from contextlib import contextmanager

from fastapi import FastAPI, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel, EmailStr

# ---------------------------------------------------------------------------
# Configuration — all secrets come from environment variables
# ---------------------------------------------------------------------------
API_KEY: str = os.getenv("API_KEY", "")
DATABASE_URL: str = os.getenv("DATABASE_URL", "users.db")

# ---------------------------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------------------------
app = FastAPI(
    title="User Service",
    description="Modernised user-lookup microservice",
    version="2.0.0",
)

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# ---------------------------------------------------------------------------
# Pydantic response models
# ---------------------------------------------------------------------------

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr


class HealthResponse(BaseModel):
    status: str

class ErrorResponse(BaseModel):
    detail: str

# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------

def _init_db(conn: sqlite3.Connection) -> None:
    """Ensure the users table exists (useful for test/dev environments)."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    NOT NULL,
            email    TEXT    NOT NULL
        )
        """
    )
    conn.commit()


@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    _init_db(conn)
    try:
        yield conn
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Security dependency
# ---------------------------------------------------------------------------

def verify_api_key(key: str = Security(api_key_header)) -> str:
    """Validate the X-API-Key header when API_KEY env-var is configured."""
    if API_KEY and key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
    return key


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/health", response_model=HealthResponse, tags=["ops"])
def health_check():
    """Liveness probe — always returns 200 when the service is running."""
    return {"status": "ok"}


@app.get(
    "/api/v2/users/{user_id}",
    response_model=UserResponse,
    responses={
        404: {"model": ErrorResponse, "description": "User not found"},
        401: {"model": ErrorResponse, "description": "Unauthorised"},
    },
    tags=["users"],
    dependencies=[Security(verify_api_key)],
)
def get_user(user_id: int):
    """
    Retrieve a single user by their integer ID.

    - **user_id**: path parameter (integer); FastAPI validates the type
      automatically — non-integer values yield 422 Unprocessable Entity.
    """
    with get_db() as conn:
        # Parameterised query — user input never interpolated into SQL string
        cursor = conn.execute(
            "SELECT id, username, email FROM users WHERE id = ?",
            (user_id,),
        )
        row = cursor.fetchone()

    if row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id={user_id} not found",
        )

    return UserResponse(id=row[0], username=row[1], email=row[2])
