#!/usr/bin/env python
from kafka import KafkaProducer
import json
from time import sleep
from datetime import datetime
import time

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: str(v).encode('utf-8'))

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
    producer.send(i[0], message)
    print ('[x] Sent %r:%r' % (i[0], message))
    time.sleep(10)
