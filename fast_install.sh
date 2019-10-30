#!/usr/bin/env bash
set -e -x
virtualenv -p python3 venv --system-site-packages --no-setuptools
venv/bin/python <(curl https://bootstrap.pypa.io/get-pip.py) --upgrade setuptools==33.1.1 zc.buildout
venv/bin/pip install -r requirements.txt
venv/bin/pip install .
