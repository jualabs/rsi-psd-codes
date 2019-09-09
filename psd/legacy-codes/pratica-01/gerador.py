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

messages = [['petrolina.radiacao-uv',4],          ['petrolina.radiacao-uv',6],
            ['petrolina.velocidade-vento',120],   ['petrolina.velocidade-vento',80],
	    ['petrolina.precipitacao',70],        ['petrolina.precipitacao',90],
            ['parnamirim.radiacao-uv',3],         ['parnamirim.radiacao-uv',2],
            ['parnamirim.velocidade-vento',60],   ['parnamirim.velocidade-vento',130],
            ['parnamirim.precipitacao',110],      ['parnamirim.precipitacao',90],
            ['serra-talhada.radiacao-uv',7],      ['serra-talhada.radiacao-uv',3],
            ['serra-talhada.velocidade-vento',90],['serra-talhada.velocidade-vento',80],
            ['serra-talhada.precipitacao',120],   ['serra-talhada.precipitacao',90],
            ['pesqueira.radiacao-uv',4],          ['pesqueira.radiacao-uv',3],
            ['pesqueira.velocidade-vento',160],   ['pesqueira.velocidade-vento',80],
            ['pesqueira.precipitacao',90],        ['pesqueira.precipitacao',70],
            ['recife.radiacao-uv',3],             ['recife.radiacao-uv',4],
            ['recife.velocidade-vento',70],       ['recife.velocidade-vento',70],
            ['recife.precipitacao',120],          ['recife.precipitacao',80]]

for i in messages:
	message = '%d,%d' % (time.time(), i[1])
	channel.basic_publish(exchange='topic_logs', routing_key=i[0], body=message)
	print " [x] Sent %r:%r" % (i[0], message)
	time.sleep(2)

connection.close()
