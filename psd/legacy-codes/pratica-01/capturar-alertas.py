#!/usr/bin/env python
import pika
import sys
import time

if len(sys.argv) != 5 :
    print >> sys.stderr, "Usage: %s [RabbitMQ host] [RabbitMQ user] [RabbitMQ password] [RabbitMQ vhost]..." % (sys.argv[0],)
    sys.exit(1)

host = sys.argv[1]
user = sys.argv[2]
passwd = sys.argv[3]
vhost = sys.argv[4]

credentials = pika.PlainCredentials(user, passwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(host, 5672, vhost, credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare(exclusive=False)
queue_name = result.method.queue

channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key='#')

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
