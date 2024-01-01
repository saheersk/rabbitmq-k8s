import json
import uuid

import pika
from rest_framework.exceptions import AuthenticationFailed

from order.rabbitmq_connection import get_rabbitmq_connection


def send_request(queue_name, request_data):
    connection = get_rabbitmq_connection()

    try:
        channel = connection.channel()
        channel.queue_declare(queue=queue_name, durable=True)

        
        correlation_id = 'unique_correlation_id'

        request_data['correlation_id'] = correlation_id

        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps(request_data),
            properties=pika.BasicProperties(
                reply_to='response_queue',
                correlation_id=correlation_id,
            )
        )

        print(f" [x] Sent request to '{queue_name}' with correlation_id={correlation_id}")
    finally:
        connection.close()


def authenticate_user(auth_user):
    connection = get_rabbitmq_connection()

    try:
        channel = connection.channel()

        print(auth_user, "=========auth_user========")
        correlation_id = str(uuid.uuid4())
        auth_user['correlation_id'] = correlation_id


        reply_queue = channel.queue_declare(queue='', exclusive=True)

        # Set up a consumer to listen for the response
        def callback(ch, method, properties, body):
            if properties.correlation_id == correlation_id:
                ch.user_response = json.loads(body)

        channel.basic_consume(queue=reply_queue.method.queue, on_message_callback=callback, auto_ack=True)

        # Publish the authentication request
        channel.basic_publish(
            exchange='',
            routing_key='request_queue',
            body=json.dumps(auth_user),
            properties=pika.BasicProperties(
                reply_to=reply_queue.method.queue,
                correlation_id=correlation_id,
            )
        )

        print(f" [x] Sent request to '{reply_queue.method.queue}' with correlation_id={correlation_id}")

        # Wait for the response
        while not hasattr(channel, 'user_response'):
            connection.process_data_events(time_limit=1)

        # Check the response
        user_response = getattr(channel, 'user_response', None)
        print(user_response, "==========user_response========")
        if not user_response or not user_response.get('authenticated'):
            raise AuthenticationFailed('Invalid authentication token')

        return user_response['user']

    finally:
        connection.close()
