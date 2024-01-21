#! /bin/bash

python manage.py migrate --no-input

python manage.py collectstatic --no-input

exec gunicorn config.wsgi:application -b 0.0.0.0:8080 --reload