#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('avaliacaoparcial2', 'voutirar10')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '172.16.207.146', 5672, 'meteorologia', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue







binding_keys = '*.*'

channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
        		routing_key = binding_keys)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    sensor = method.routing_key.split(".") 
    valor = body.split(",")
    print ("Cidade %r Sensor %r, Timestamp %r Valor %r" % (sensor[0],sensor[1], valor[0], valor[1]))
    if sensor[1] == "precipitacao" and int(valor[1]) > 100:
	channel.basic_publish(exchange="topic_logs", 
	routing_key="%r.alerta.inundacao" % (sensor[0]), 
	body=valor[1]+','+valor[0])
    elif sensor[1] == "velocidade-vento" and int(valor[1]) > 100:
	channel.basic_publish(exchange="topic_logs", 
        routing_key="%r.alerta.ventania" % (sensor[0]), 
        body=valor[1]+','+valor[0])
    elif sensor[1] == "radiacao-uv" and int(valor[1]) > 5:
	channel.basic_publish(exchange="topic_logs", 
	routing_key="%r.alerta.insolacao" % (sensor[0]), 
	body=valor[1]+','+valor[0])
    

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
