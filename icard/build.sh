#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python icard/manage.py collectstatic --no-input
python icard/manage.py migrate