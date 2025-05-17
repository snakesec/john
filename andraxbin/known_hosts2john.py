#!/bin/bash

source /opt/ANDRAX/john/venv/bin/activate

/opt/ANDRAX/john/venv/bin/python3 /opt/ANDRAX/john/known_hosts2john.py "$@"

