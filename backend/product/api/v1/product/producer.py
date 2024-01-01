import json

import pika

from product.rabbitmq_connection import get_rabbitmq_connection


def send_create_order(product_details):
    connection = get_rabbitmq_connection()

    try:
        channel = connection.channel()

        channel.exchange_declare(exchange='user_create_order_exchange', exchange_type='direct')

        message_body = json.dumps(product_details)

        channel.basic_publish(
            exchange='user_create_order_exchange',
            routing_key="create_order_key",
            body=message_body,
            properties=pika.BasicProperties(
                delivery_mode=2, 
            )
        )

        print(f" [x] Sent create order message: {message_body}")

    finally:
        connection.close()


