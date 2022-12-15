#!/usr/bin/env bash
# exit on error
set -o errexit

poetry self update @1.3.1
poetry install

python manage.py collectstatic --no-input
python manage.py migrate