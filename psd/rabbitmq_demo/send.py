#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='temperature')

channel.basic_publish(exchange='',
                      routing_key='temperature',
                      body='quente')
print " [x] Sent 'Hello World!'"
connection.close()
