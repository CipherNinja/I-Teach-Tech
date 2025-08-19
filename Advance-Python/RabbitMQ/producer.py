from colorama import init, Fore, Style
import pika

init(autoreset=True)

def connect_to_rabbitmq():
    print("🔌 Connecting to RabbitMQ...")
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    return connection, channel

def declare_queue(channel, queue_name='task_queue'):
    print(f"Declaring queue: {queue_name}")
    channel.queue_declare(queue=queue_name, durable=True)

def send_task(channel, queue_name='task_queue', message='First task: process aircraft log file'):
    print(f"📤 Sending task: {message}")
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)
    )
    print("✅ Task sent successfully!")

def main():
    try:
        connection, channel = connect_to_rabbitmq()
        declare_queue(channel)
        send_task(channel)
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        connection.close()
        print("🔒 Connection closed.")

if __name__ == "__main__":
    main()
