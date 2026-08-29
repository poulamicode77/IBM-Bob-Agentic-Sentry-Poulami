# legacy_app.py - Outdated Monolithic Service
import json
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
SECRET_API_KEY = "DEV_SECRET_12345_DO_NOT_LEAK"  # Security flaw: Hardcoded secret


def get_db():
  return sqlite3.connect("users.db")


# Deprecated routing & no request validation
@app.route("/api/v1/get_user", methods=["GET"])
def fetch_user():
  user_id = request.args.get("id")
  conn = get_db()
  cursor = conn.cursor()
  # Security flaw: Direct SQL string injection vulnerability
  query = f"SELECT id, username, email FROM users WHERE id = '{user_id}'"
  cursor.execute(query)
  row = cursor.fetchone()
  conn.close()

  if not row:
    return jsonify({"error": "User missing"}), 404
  return jsonify({"id": row[0], "username": row[1], "email": row[2]}), 200


if __name__ == "__main__":
  app.run(port=5000, debug=True)