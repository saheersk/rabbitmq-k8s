#!/bin/bash

# Start the Django application
gunicorn -c product/gunicorn_config.py product.wsgi:application
