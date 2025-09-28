#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# Force migrations
python manage.py migrate --verbosity=2
python manage.py migrate --run-syncdb --verbosity=2

python manage.py collectstatic --clear --noinput