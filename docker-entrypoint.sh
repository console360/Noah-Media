#!/bin/sh

python3 manage.py migrate
python3 ./noah/setup_database.py
python3 manage.py collectstatic --noinput
service nginx start
exec uwsgi --ini uwsgi.ini
