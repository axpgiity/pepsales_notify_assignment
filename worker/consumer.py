import pika, json, time
from app.utils.database import notifications_db

def deliver(notification):
    if notification["type"] == "email":
        print(f"Email: {notification['message']}")
    elif notification["type"] == "sms":
        print(f"SMS: {notification['message']}")
    elif notification["type"] == "inapp":
        print(f"In-App: {notification['message']}")
    notifications_db.append(notification)

def callback(ch, method, properties, body):
    try:
        data = json.loads(body)
        deliver(data)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print("Error processing message:", e)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue='notifications', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="notifications", on_message_callback=callback)
    print("Worker started. Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    consume()