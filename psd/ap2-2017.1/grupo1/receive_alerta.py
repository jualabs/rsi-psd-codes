#!/usr/bin/env python
import pika
import sys

routing_keys = ['petrolina.radiacao-uv','petrolina.radiacao-uv',
                 'petrolina.velocidade-vento','petrolina.velocidade-vento',
		 		 'petrolina.precipitacao','petrolina.precipitacao',
		 		 'parnamirim.radiacao-uv','parnamirim.radiacao-uv',
                 'parnamirim.velocidade-vento','parnamirim.velocidade-vento',
                 'parnamirim.precipitacao','parnamirim:.precipitacao',
                 'serra-talhada.radiacao-uv','serra-talhada.radiacao-uv',
                 'serra-talhada.velocidade-vento','serra-talhada.velocidade-vento',
                 'serra-talhada.precipitacao','serra-talhada.precipitacao',
                 'pesqueira.radiacao-uv','pesqueira.radiacao-uv',
                 'pesqueira.velocidade-vento','pesqueira.velocidade-vento',
                 'pesqueira.precipitacao','pesqueira.precipitacao',
                 'recife.radiacao-uv','recife.radiacao-uv',
                 'recife.velocidade-vento','recife.velocidade-vento',
                 'recife.precipitacao','recife.precipitacao']

credentials = pika.PlainCredentials('avaliacaoparcial2', 'voutirar10')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '172.16.206.77', 5672, 'meteorologia', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

for binding_key in routing_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body)
    cidade, sensor = method.routing_key.split('.')
    timestamp, valor = body.split(",")
    if sensor == "precipitacao" and int(valor) > 100:
	channel.basic_publish(exchange='topic_logs',
                      routing_key=cidade+".alerta.inundacao",
                      body=valor+","+timestamp)
    elif sensor == "velocidade-vento" and int(valor) > 100:
        channel.basic_publish(exchange='topic_logs',
                      routing_key=cidade+".alerta.ventania",
                      body=valor+","+timestamp)
    elif sensor == "radiacao-uv" and int(valor) > 5:
        channel.basic_publish(exchange='topic_logs',
                      routing_key=cidade+".alerta.insolacao",
                      body=valor+","+timestamp)
     

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
