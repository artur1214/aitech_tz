#!/bin/sh

cd /app


# Setup django
python manage.py makemigrations
python manage.py migrate
#python manage.py populate #From old project
# Run Django server with gunicorn
gunicorn --workers=8 configs.wsgi:application --reload --bind 0.0.0.0:5000