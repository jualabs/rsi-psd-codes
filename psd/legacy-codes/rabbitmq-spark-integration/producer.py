import pika
import time 

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
# credentials = pika.PlainCredentials('vwcm', 'vwcm')
# connection = pika.BlockingConnection(pika.ConnectionParameters(
#               'localhost', 5672, 'psd', credentials))
channel = connection.channel()
channel.exchange_declare(exchange='amq.topic',
                 exchange_type='topic', durable=True)

for i in range(1000):
    channel.basic_publish(
        exchange='amq.topic',  # amq.topic as exchange
        routing_key='hello',   # Routing key used by producer
        body='Hello World {0}'.format(i)
    )
    time.sleep(1)

connection.close()
