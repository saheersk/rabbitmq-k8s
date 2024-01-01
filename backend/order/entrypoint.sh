#!/bin/bash

# Start the Django application
gunicorn -c order/gunicorn_config.py order.asgi:application
python manage.py consume_messages
