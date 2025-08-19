import pika

# RabbitMQ server se connect hona (default port: 5672)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Queue create karna (agar exist nahi karta)
channel.queue_declare(queue='test_queue')

# Message bhejna
message = "Hello from Producer!"
channel.basic_publish(exchange='',
                      routing_key='test_queue',
                      body=message)

print(f" [x] Sent: {message}")

# Connection close
connection.close()



# import pika
# import json

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# channel.queue_declare(queue='task_queue', durable=True)

# data = {"task": "process_order", "order_id": 123}
# channel.basic_publish(
#     exchange='',
#     routing_key='task_queue',
#     body=json.dumps(data),
#     properties=pika.BasicProperties(delivery_mode=2)
# )

# print(" [x] Sent:", data)
# connection.close()
