#!/usr/bin/evn bash

set -o errexit

pip3 install -r dependencies.txt

python3 manage.py migrate