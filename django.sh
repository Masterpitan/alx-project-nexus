#!/bin/bash
set -e

echo "Starting Gunicorn server..."
exec gunicorn social_feed.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2
