#!/usr/bin/env python
import pika
import sys

if len(sys.argv) != 4 :
    print >> sys.stderr, "Usage: %s [CloudAMQP Host] [CloudAMQP: User & Vhost] [CloudAMQP Password]..." % (sys.argv[0],)
    sys.exit(1)

host = sys.argv[1]
user_vhost = sys.argv[2]
passwd = sys.argv[3]

credentials = pika.PlainCredentials(user_vhost, passwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(host, 5672, user_vhost, credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key='*.alerta.*')

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
