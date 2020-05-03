#!/bin/bash
pip install -r requirements.txt

python manage.py migrate

gunicorn currencyapp.wsgi:application --bind 0.0.0.0:8000 --timeout 600 --workers 3 --log-level=info