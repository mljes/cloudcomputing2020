#!/bin/bash

cd sharebook
source venv/bin/activate
export FLASK_ENV=development
export FLASK_APP=controller/app.py
flask run -h 0.0.0.0
