#!/usr/bin/env python
import pika
import sys
import time

ip_rabbitmq_server = sys.argv[1] 

if not ip_rabbitmq_server:
    print >> sys.stderr, "Usage: %s [rabbitmq_server_ip]..." % (sys.argv[0],)
    sys.exit(1)

credentials = pika.PlainCredentials('avaliacaoparcial2', 'voutirar10')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               ip_rabbitmq_server, 5672, 'meteorologia', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

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
values = [4,6,120,80,70,90,  # radiacao-petrolina 6, vento-petrolina 120
          3,2,60,130,110,90, # vento-parnamirim 130, chuva-parnamirim 110
          7,3,90,80,120,90,  # radiacao-serra 7, chuva-serra 120
          4,3,160,80,90,70,  # vento-pesquira 160
	  3,4,70,70,120,80]  # chuva-recife 120
 
for i in range(0, 29):
	message = '%d,%d' % (time.time(), values[i])
	channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_keys[i],
                      body=message)
	print " [x] Sent %r:%r" % (routing_keys[i], message)
	time.sleep(2)
connection.close()
