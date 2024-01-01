import json
import uuid

import requests
import pika
from celery import shared_task
from celery.signals import worker_ready

from authentication.rabbitmq_connection import get_rabbitmq_connection


def authenticate_user_logic(auth_request):

    print(auth_request, "========auth_request logic===============")
    auth_token = auth_request.get('token')


    if not auth_token:
        return False  # Token not provided

    # Make a request to the /token/verify API
    verify_url = 'http://localhost:8000/token/verify/'  # Replace with your actual API endpoint
    headers = {'Authorization': f'Token {auth_token.token}'}

    try:
        response = requests.post(verify_url, headers=headers)
        response_data = response.json()

        # Check the response for successful verification
        if response.status_code == 200 and response_data.get('valid'):
            return True  # Authentication successful
        else:
            return False  # Authentication failed
    except requests.RequestException:
        return False
    
def authenticate_user_callback(ch, method, properties, body):
    auth_request = json.loads(body)

    print(auth_request, "======auth_request Authentication request===========")
    authenticated = authenticate_user_logic(auth_request)

    # Prepare the response message
    response_message = {
        "authenticated": authenticated,
    }

    # Send back the response to the specified reply_to queue
    ch.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(
            correlation_id=properties.correlation_id
        ),
        body=json.dumps(response_message)
    )

    print(f" [x] Sent authentication response with correlation_id={properties.correlation_id}")

@shared_task
def task_verify_auth():
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    queue_name = 'request-queue'
    channel.queue_declare(queue=queue_name, exclusive=True)

    channel.basic_consume(queue=queue_name, on_message_callback=authenticate_user_callback, auto_ack=True)

    print(' [*] Waiting for authentication requests. To exit press CTRL+C')
    channel.start_consuming()

# @worker_ready.connect
# def on_worker_init(**kwargs):
#     print("Celery worker of authentication process is initializing. Performing initialization tasks...")
#     task_verify_auth.apply_async()
    