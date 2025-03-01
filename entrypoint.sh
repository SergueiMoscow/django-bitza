#!/bin/sh
# Apply database migrations
echo "Installing dependencies"
poetry install --no-root

echo "Applying database migrations"
poetry run python manage.py migrate --no-input

# Start the main process
echo "Starting application"
poetry run gunicorn bitza.asgi:application -k uvicorn.workers.UvicornWorker -b :8087
