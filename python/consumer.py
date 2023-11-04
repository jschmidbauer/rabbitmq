import pika

def on_message_received(ch, method, properties, body):
    print(f"Received new message: {body}")

creds = pika.PlainCredentials('guest', 'guest')

connection_parameters = pika.ConnectionParameters(host="localhost", credentials=creds)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)

print("Started consuming")

channel.start_consuming()
