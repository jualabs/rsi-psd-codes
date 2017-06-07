#/usr/bin/env python
import pika

credentials = pika.PlainCredentials('vwcm', 'vwcm')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost', 5672, 'psd', credentials))
channel = connection.channel()


channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
