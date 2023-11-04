import pika

creds = pika.PlainCredentials('guest', 'guest')

connection_parameters = pika.ConnectionParameters(host="localhost", credentials=creds)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


channel.queue_declare(queue='letterbox')

message = "Hello from Rabbitmq"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"sent message: {message}")

connection.close





