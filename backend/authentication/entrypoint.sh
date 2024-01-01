#!/bin/bash

# Start the Django application
gunicorn -c authentication/gunicorn_config.py authentication.wsgi:application
