import pika, os
import json


url = os.environ.get('CLOUDAMQP_URL', 'amqp://fxpccdrd:NJiudHhok5U_IISeM9pRqumppBFsk5Q1@wildboar.rmq.cloudamqp.com/fxpccdrd')
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='esd', durable=True)


def callback(ch, method, properties, body):
    #data = json.loads(body)
    print(" [x] Received :" + json.dumps(json.loads(body)))


channel.basic_consume(
    queue='esd', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()