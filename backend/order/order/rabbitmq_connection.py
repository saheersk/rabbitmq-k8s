import pika
from django.conf import settings

def get_rabbitmq_connection():
    print(" [*] Connecting to RabbitMQ...")
    credentials = pika.PlainCredentials(
        username=settings.RABBITMQ_USERNAME,
        password=settings.RABBITMQ_PASSWORD
    )

    parameters = pika.ConnectionParameters(
        host=settings.RABBITMQ_HOST,
        port=settings.RABBITMQ_PORT,
        virtual_host=settings.RABBITMQ_VIRTUAL_HOST,
        credentials=credentials
    )

    try:
        connection = pika.BlockingConnection(parameters)
        print(" [*] RabbitMQ Connection established.")
        return connection
    except Exception as e:
        print(f" [x] Error connecting to RabbitMQ: {e}")
        raise
