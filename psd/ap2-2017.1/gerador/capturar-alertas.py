#!/usr/bin/env python
import pika
import sys

ip_rabbitmq_server = sys.argv[1]

if not ip_rabbitmq_server:
    print >> sys.stderr, "Usage: %s [rabbitmq_server_ip] [routing_keys]" % (sys.argv[0],)
    sys.exit(1)

credentials = pika.PlainCredentials('avaliacaoparcial2', 'voutirar10')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               ip_rabbitmq_server, 5672, 'meteorologia', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

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
