# order/tasks.py
import pika
import json

from celery import shared_task
from celery.signals import worker_ready

from order.rabbitmq_connection import get_rabbitmq_connection
from user_order.models import Order


@shared_task
def receive_login_messages():
    connection = get_rabbitmq_connection()

    try:
        channel = connection.channel()

        # Declare the fanout exchange
        channel.exchange_declare(exchange='user_login_exchange', exchange_type='fanout')

        # Declare a unique queue for this service
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        # Bind the queue to the fanout exchange
        channel.queue_bind(exchange='user_login_exchange', queue=queue_name)

        print("[*] Waiting for login messages. To exit press CTRL+C")

        def callback(ch, method, properties, body):
            print(f" [x] Received login message: {body}")

        # Set up the callback function to handle incoming messages
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        # Start consuming messages
        channel.start_consuming()
    finally:
        connection.close()


def handle_create_order(ch, method, properties, body):
    product_details = json.loads(body)
    print(product_details, "product_details")
    Order.objects.create(
        user_id=int(product_details['user_id']),
        product_name=product_details['product_name'],
        quantity=1,
    )

    print(f"Received create order message: {product_details}")


@shared_task
def consume_create_order_messages():
    connection = get_rabbitmq_connection()

    try:
        channel = connection.channel()

        channel.exchange_declare(exchange='user_create_order_exchange', exchange_type='direct')

        # Declare a unique queue for this consumer
        result = channel.queue_declare(queue='create_order_queue', exclusive=True)
        queue_name = result.method.queue

        # Bind the queue to the exchange with the specific routing key
        channel.queue_bind(exchange='user_create_order_exchange', queue=queue_name, routing_key='create_order_key')

        print(" [*] Waiting for create order messages. To exit press CTRL+C")

        # Set up the callback function to handle incoming messages
        channel.basic_consume(queue=queue_name, on_message_callback=handle_create_order, auto_ack=True)

        # Start consuming messages
        channel.start_consuming()

    finally:
        connection.close()


@worker_ready.connect
def on_worker_ready(sender, **kwargs):
    print("Celery worker of Order is ready. Performing initialization tasks...")
    receive_login_messages.apply_async()
    consume_create_order_messages.apply_async()