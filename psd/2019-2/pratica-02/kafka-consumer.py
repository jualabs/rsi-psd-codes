from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'petrolina.radiacao-uv',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=False,
     group_id='my-group',
     value_deserializer=lambda v: str(v).encode('utf-8'))

for message in consumer:
    message = message.value
    print('received: ' + str(message))