#!/bin/bash
set -e

echo "==> Running migrations..."
python manage.py migrate --noinput

echo "==> Seeding demo users..."
python manage.py seed_users || echo "  (seed already applied or skipped)"

echo "==> Collecting static files..."
python manage.py collectstatic --noinput

echo "==> Starting gunicorn on 0.0.0.0:7860..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:7860 \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
