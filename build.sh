#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py setup_db
python manage.py collectstatic --clear --noinput --verbosity 2