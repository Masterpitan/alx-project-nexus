#!/bin/bash
set -e

echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Running migrations..."
python manage.py makemigrations
echo "Applying migrations..."
python manage.py migrate

echo "Starting your server..."
python manage.py runserver 0.0.0.0:8000
