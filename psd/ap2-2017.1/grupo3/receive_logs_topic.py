#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('avaliacaoparcial2', 'voutirar10')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '172.16.205.243', 15672, 'meteorologia', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue
#routing_key = sys.argv[1]


valor= body.split(",")
tipo= method.routing_key.split(".")
if (len(sys.argv) == 2):
	if((valor[1] > 100) and (tipo[1] == "precipitacao")):
		message= valor[1] + "." + valor[0];
		routing_key= tipo[0] + ".alerta." + tipo[1]; 
	if((valor[1] > 100) and (tipo[1] == "velocidade-vento")):
		message= valor[1] + "." + valor[0];
		routing_key= tipo[0] + ".alerta." + tipo[1];
	if((valor[1] > 5) and (tipo[1] == "radiacao-uv")):
		message= valor[1] + "." + valor[0];
		routing_key= tipo[0] + ".alerta." + tipo[1];
	chanel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message);

#binding_keys = sys.argv[1:]
#if not binding_keys:
#    print >> sys.stderr, "Usage: %s [binding_key]..." % (sys.argv[0],)
#    sys.exit(1)

#for binding_key in binding_keys:
#    channel.queue_bind(exchange='topic_logs',
#                       queue=queue_name,
#                       routing_key=binding_key)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
