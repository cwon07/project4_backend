#!/usr/bin/evn bash

set -o errexit

pip install -r dependencies.txt

python manage.py migrate