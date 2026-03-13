FROM python:3.12-slim

LABEL maintainer="LorcanTuo"
LABEL description="IT Tasker — lightweight IT ticket tracker"

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create a non-root user to run the app
RUN adduser --disabled-password --no-create-home appuser \
    && mkdir -p /app/data \
    && chown -R appuser:appuser /app
USER appuser

# Database will live in /app/data so it can be mounted as a volume
ENV DATABASE_PATH=/app/data

EXPOSE 5001

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5001/login')" || exit 1

CMD ["python", "app.py"]
