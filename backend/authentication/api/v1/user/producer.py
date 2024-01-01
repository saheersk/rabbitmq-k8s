import json

from authentication.rabbitmq_connection import get_rabbitmq_connection


def send_login_message(user_details):
    connection = get_rabbitmq_connection()

    try:
        channel = connection.channel()

        channel.exchange_declare(exchange='user_login_exchange', exchange_type='fanout')

        # Convert user_details to a JSON string
        user_message = json.dumps(user_details)

        channel.basic_publish(exchange='user_login_exchange', routing_key='', body=user_message)

        print(f" [x] Sent login message for user '{user_details}'")
    finally:
        connection.close()


def send_signup_message(signup_details):
    connection = get_rabbitmq_connection()

    try:
        channel = connection.channel()

        channel.exchange_declare(exchange='user_signup_exchange', exchange_type='fanout')

        signup_message = json.dumps(signup_details)

        channel.basic_publish(exchange='user_signup_exchange', routing_key='', body=signup_message)

        print(f" [x] Sent login message for user '{signup_details}'")
    finally:
        connection.close()
