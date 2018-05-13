#/usr/bin/env python
import pika

credentials = pika.PlainCredentials('uitsdbkq', 'oVMBBKTj_Axu6BqIArCWs79oNtxIJGvH')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'fox.rmq.cloudamqp.com', 5672, 'uitsdbkq', credentials))
channel = connection.channel()


channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
