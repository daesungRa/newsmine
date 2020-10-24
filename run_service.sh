#!/usr/bin/env bash
PJT_DIR="$( cd "$( dirname "$( readlink -f "${BASH_SOURCE[0]}" )" )" && pwd )"
export PYTHONPATH="$PJT_DIR"
cd "$PJT_DIR"

service nginx reload
service nginx restart

. ./venv/bin/activate  # in ubuntu
# . ./venv/Scripts/activate  # in windows
gunicorn --workers 1 --threads 8 --worker-class gevent --timeout 30 --name newsmine newsmine.server:app

