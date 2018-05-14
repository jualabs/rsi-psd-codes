#!/usr/bin/env python
import pika
import sys
import time

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

messages = {'petrolina.radiacao-uv':4,          'petrolina.radiacao-uv':6,
            'petrolina.velocidade-vento':120,   'petrolina.velocidade-vento':80,
		 	'petrolina.precipitacao':70,        'petrolina.precipitacao':90,
		 	'parnamirim.radiacao-uv':3,         'parnamirimradiacao-uv':2,
            'parnamirim.velocidade-vento':60,   'parnamirim.velocidade-vento':130,
            'parnamirim.precipitacao':110,      'parnamirim.precipitacao':90,
            'serra-talhada.radiacao-uv':7,      'serra-talhada.radiacao-uv':3,
            'serra-talhada.velocidade-vento':90,'serra-talhada.velocidade-vento':80,
            'serra-talhada.precipitacao':120,   'serra-talhada.precipitacao':90,
            'pesqueira.radiacao-uv':4,          'pesqueira.radiacao-uv':3,
            'pesqueira.velocidade-vento':160,   'pesqueira.velocidade-vento':80,
            'pesqueira.precipitacao':90,        'pesqueira.precipitacao':70,
            'recife.radiacao-uv':3,             'recife.radiacao-uv':4,
            'recife.velocidade-vento':70,       'recife.velocidade-vento':70,
            'recife.precipitacao':120,          'recife.precipitacao':80}

for k,v in messages.iteritems():
	message = '%d,%d' % (time.time(), v)
	channel.basic_publish(exchange='topic_logs', routing_key=k, body=message)
	print " [x] Sent %r:%r" % (k, message)
	time.sleep(2)

connection.close()
