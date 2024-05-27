#!/bin/bash
source env/bin/activate
gunicorn --workers 3 --bind 0.0.0.0:8000 myproject.wsgi
