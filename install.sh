#!/bin/bash

rm -rf .env # clean out any old materials

brew install python@3.8
/usr/local/Cellar/python@3.8/3.8.18/bin/python3.8 -m venv .env

source .env/bin/activate

pip install --upgrade pip

# install auditorium and related dependencies
pip install "uvicorn==0.18.2" "markupsafe==2.0.1" auditorium

# install other dependencies used for this project
pip install numpy matplotlib

# Make sure Auditorium is working after all that
auditorium demo