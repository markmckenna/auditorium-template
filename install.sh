#!/bin/bash

brew install python@3.8
/usr/local/Cellar/python@3.8/3.8.18/bin/python3.8 -m venv .env
source .env/bin/activate
pip install --upgrade pip
pip install "uvicorn==0.18.2" "markupsafe==2.0.1" auditorium

./start.sh