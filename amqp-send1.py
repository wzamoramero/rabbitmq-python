#!/usr/bin/env python
#https://github.com/rabbitmq/rabbitmq-tutorials/blob/master/python/send.py

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()# -*- coding: utf-8 -*-

