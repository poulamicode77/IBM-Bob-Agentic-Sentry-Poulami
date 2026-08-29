# ── Stage: runtime ────────────────────────────────────────────────────────────
FROM python:3.11-slim AS runtime

# Keeps Python from buffering stdout/stderr (important for container logs)
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install dependencies first (layer-cached until requirements change)
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy application source
COPY modern_app.py ./

# Non-root user for least-privilege execution
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

# Runtime secrets — set these via docker run -e or an orchestrator secret
ENV API_KEY=""
ENV DATABASE_URL="users.db"

EXPOSE 8000

# Uvicorn with a single worker; scale horizontally via replicas
CMD ["uvicorn", "modern_app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
