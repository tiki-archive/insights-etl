#!/bin/bash

echo "hello world"

set -e

virtualenv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
deactivate
