#!/bin/bash

set -e

virtualenv virtualenv:wq
source virtualenv/bin/activate
pip install -r requirements.txt
deactivate