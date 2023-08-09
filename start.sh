#!/bin/bash

export CPU_COUNT=`grep -c ^processor /proc/cpuinfo `
export WORKER_COUNT=${WORKER_COUNT:-$(( $CPU_COUNT + 2 ))}
export MAX_REQUESTS=${MAX_REQUESTS:-2500}

python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn -b 0.0.0.0:8000 -w "$WORKER_COUNT" --max-requests "$MAX_REQUESTS" core.wsgi:application
