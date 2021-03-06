#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Mon 06 Jul 2020 09:23:48 AM CST

# File Name: 01-simplesender.py
# Description:

"""
import pika
import sys

credentials = pika.PlainCredentials('admin','Zhu88jie')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',credentials=credentials))

channel = conn.channel()
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs', 
                      routing_key=routing_key, 
                      body=message,
                      )
print(" [x] Sent {0} {1}".format(routing_key, message))

conn.close()
