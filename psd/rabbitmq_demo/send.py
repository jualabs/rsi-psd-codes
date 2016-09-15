#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('<user>', '<passwd>')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '<host_adress>', 5672, '<vhost_name>', credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
