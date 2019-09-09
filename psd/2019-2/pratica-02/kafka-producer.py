from kafka import KafkaProducer
import json
from time import sleep
from datetime import datetime
import lorem
import time

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: str(v).encode('utf-8'))

# Call the producer.send method with a producer-record
print("ctrl+c to stop...")
while True:
    message = lorem.sentence()
    producer.send('meu.topico.legal', message)
    print('sent: ' + message)
    time.sleep(10)