from colorama import init, Fore, Style
import pika

init(autoreset=True)

def connect_to_rabbitmq():
    print("🔌 Connecting to RabbitMQ...")
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    return connection, channel

def declare_queue(channel, queue_name='task_queue'):
    print(f"📦 Ensuring queue exists: {queue_name}")
    channel.queue_declare(queue=queue_name, durable=True)

def process_task(ch, method, properties, body):
    task = body.decode()
    print(f"📥 Received task: {task}")
    # Optional: Add keyword flagging or save to file here
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consumer(channel, queue_name='task_queue'):
    print("🔄 Waiting for tasks. Press CTRL+C to exit.")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=process_task)
    channel.start_consuming()

def main():
    try:
        connection, channel = connect_to_rabbitmq()
        declare_queue(channel)
        start_consumer(channel)
    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user.")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        try:
            connection.close()
            print("🔒 Connection closed.")
        except:
            pass

if __name__ == "__main__":
    main()
