#!/usr/bin/env bash
service nginx start
uwsgi --processes 1 --enable-threads --threads 8 --single-interpreter --disable-logging --ini /app/uwsgi.ini --plugin python3 -s /tmp/uwsgi.sock --uid www-data --gid www-data  &
sleep infinity
