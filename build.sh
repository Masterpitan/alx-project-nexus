#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --clear --noinput --verbosity 2
python manage.py migrate --verbosity 2