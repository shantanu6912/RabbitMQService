import pika
import json

# RabbitMQ connection parameters
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'
MQTT_TOPIC = 'devices/data'  # Example MQTT topic to publish to

# Sample data to publish
data = {
    #"id":"LIGHT#2","state":1
    "type":"retrive"
}

# Convert data to JSON format
message_body = json.dumps(data)

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST,
                                                               port=RABBITMQ_PORT,
                                                               credentials=pika.PlainCredentials(username=RABBITMQ_USERNAME,
                                                                                                  password=RABBITMQ_PASSWORD)))
channel = connection.channel()

# Declare the exchange
channel.exchange_declare(exchange='amq.topic', exchange_type='topic',  durable=True)

# Publish the message
channel.basic_publish(exchange='amq.topic', routing_key=MQTT_TOPIC, body=message_body)

print("Data published to RabbitMQ:", message_body)

# Close connection
connection.close()
