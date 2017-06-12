#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('avaliacaoparcial2', 'voutirar10')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '172.16.207.146', 5672, 'meteorologia', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic',
                         type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Temperatura'
channel.basic_publish(exchange='topic',
                      routing_key=routing_key,
                      body=message)
print " [x] Sent %r:%r" % (routing_key, message)
connection.close()
