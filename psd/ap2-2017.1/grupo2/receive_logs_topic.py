#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('avaliacaoparcial2', 'voutirar10')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '172.16.206.24', 5672, 'meteorologia', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_key = '*.*'
channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)
    cidade, tiposensor = method.routing_key.split(".")
    time, valor = body.split(",")

    if tiposensor == "radiacao-uv" and int(valor) > 5:
       print "insolacao"
       topico = cidade + ".alerta." + "insolacao"
       mensagem = valor + "," + time
       enviar(topico,mensagem)
    elif tiposensor == "velocidade-vento" and int(valor) > 100:
       print "ventania"
       topico = cidade + ".alerta." + "ventania"
       mensagem = valor + "," + time
       enviar(topico,mensagem)
    elif tiposensor == "precipitacao" and int(valor) > 100:
       print "inundacao"
       topico = cidade + ".alerta." + "inundacao"
       mensagem = valor + "," + time
       enviar(topico,mensagem)

def enviar (topico, mensagem):
    channel.basic_publish(exchange="topic_logs",
                              routing_key = topico,
                              body = mensagem)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
