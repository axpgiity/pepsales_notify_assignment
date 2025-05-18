import pika, json
from app.schemas.notification import NotificationCreate

def publish_notification(notification: NotificationCreate):
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue='notifications', durable=True)
    channel.basic_publish(
        exchange="",
        routing_key="notifications",
        body=json.dumps(notification.dict())
        properties=pika.BasicProperties(delivery_mode=2)  # persistentbt
    )
    connection.close()