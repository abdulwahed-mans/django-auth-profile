FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SECRET_KEY=hf-space-auto-generated-key-change-me-in-production \
    DEBUG=False \
    ALLOWED_HOSTS=".hf.space,localhost,127.0.0.1" \
    SECURE_SSL_REDIRECT=False \
    CSRF_TRUSTED_ORIGINS="https://abdulwahed-sweden-django-auth-profile.hf.space" \
    PORT=7860

# Create non-root user
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Remove files that shouldn't be in the image
RUN rm -rf venv/ .env __pycache__ db.sqlite3 .git/

# Create directories and set permissions
RUN mkdir -p /app/staticfiles && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Make startup script executable
RUN chmod +x startup.sh

EXPOSE 7860

CMD ["./startup.sh"]
