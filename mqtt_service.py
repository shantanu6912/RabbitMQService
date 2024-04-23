import pika
import pymongo
import json
import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")
# Setup logging
logging.basicConfig(level=logging.INFO,filename="logs\RabbitMQService.log")
logger = logging.getLogger(__name__)

RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'
MQTT_TOPIC = 'devices/data'  

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DATABASE = 'devices'
MONGODB_COLLECTION = 'device_data'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST,port=RABBITMQ_PORT,
                                                               credentials=pika.PlainCredentials(username=RABBITMQ_USERNAME,
                                                               password=RABBITMQ_PASSWORD)))
channel = connection.channel()

mongo_client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
db = mongo_client[MONGODB_DATABASE]
collection = db[MONGODB_COLLECTION]

def callback(ch, method, properties, body):
    try:
        message = json.loads(body)
        print("Received message:", message)
        logger.debug("Received message: "+str(message))
        if "id" in message.keys() and "LIGHT" in message["id"]:
            transformed_message = {
            'id': message['id'],
            'status': {
                'state': message['state'],
                'device_type':"LIGHT"
                }
            }
            logger.info("Transformed Message for device type LIGHT")
            collection.insert_one(transformed_message)
            logger.info("Stored data in DB "+str(transformed_message))
        elif "type" in message.keys() and message["type"] == "retrive":
            documents = collection.find()
            for dc in documents:
                print(dc)
                logger.info("retrived data from mongodb "+str(dc))
        else:
            collection.insert_one(message)
            logger.info("Stored data in DB "+str(message))
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")

channel.queue_declare(queue='mqtt_queue')
channel.queue_bind(exchange='amq.topic', queue='mqtt_queue', routing_key=MQTT_TOPIC)

channel.basic_consume(queue='mqtt_queue', on_message_callback=callback, auto_ack=True)

# Start consuming messages
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()