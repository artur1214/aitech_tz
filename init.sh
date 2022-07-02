#!/bin/sh

# Delete previosly session Celery files
cd /app
rm *.db *.pid

# Run daemons
service redis-server start
systemctl daemon-reload
systemctl enable celery.service
systemctl enable celerybeat.service
systemctl enable celeryflower.service
systemctl start celery.service
systemctl start celerybeat.service
systemctl start celeryflower.service

# Setup django
python manage.py makemigrations
python manage.py migrate
python manage.py populate
# Run Django server with gunicorn
gunicorn --workers=10 amazeme.wsgi:application --reload --bind 0.0.0.0:4480