#!/bin/bash

echo "hello world 2"

set -e

virtualenv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
deactivate
