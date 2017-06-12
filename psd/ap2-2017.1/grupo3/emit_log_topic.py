#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('avaliacaoparcial2','voutirar10')

connection = pika.BlockingConnection(pika.ConnectionParameters('172.16.205.243',5672,'meteorologia',credentials))
print('t');

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result= channel.queue_declare(exclusive=True);

queue_name= result.method.queue;

#binding_keys = "*.*";#sys.argv[1:];

#if not binding_keys:
#	print >> sys.stderr, "Usage: %s [binding_key] ..." % (sys.argv[0],)
#	sys.exit(1);

#for binding_key in binding_keys:

channel.queue_bind(exchange='topic_log', queue=queue_name, routing_key="*.*");

print(' [*] Waiting for logs. To exit press CTRL+C');

def callback(ch, method, properties, body):
	print(" [x] %r:%r" % (method.routing_key, body));
	ex();

channel.basic_consume(callback, queue=queue_name, no_ack=True);

channel.start_consuming();

valor= body.split(",");
tipo= method.ruting_key.split(".");

def ex():
	if(((valor[1] > 100) and (tipo[1] == "precipitacao")) or ((valor[1] > 100) and (tipo[1] == "velocidade-vento")) or ((valor[1] > 5) and (tipo[1] == "radiacao-uv"))):
		message= valor[1] + "." + valor[0];
		routing_key= tipo[0] + ".alerta." + tipo[1];


channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print " [x] Sent %r:%r" % (routing_key, message)
connection.close()
