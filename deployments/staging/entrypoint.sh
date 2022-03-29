#!/usr/bin/env bash

echo "Collectiong static files"
python manage.py collectstatic

echo "Starting the server"
gunicorn --reload -b 0.0.0.0:8000 config.wsgi:application --workers 3 --timeout 300 --graceful-timeout 10 --log-level info --log-file -