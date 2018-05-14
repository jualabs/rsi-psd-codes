#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('uitsdbkq', 'oVMBBKTj_Axu6BqIArCWs79oNtxIJGvH')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'fox.rmq.cloudamqp.com', 5672, 'uitsdbkq', credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
