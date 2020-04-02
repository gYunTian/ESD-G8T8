import pika, os, logging
from flask import Flask, request, make_response, jsonify
import json
from flask_cors import CORS, cross_origin

logging.basicConfig()
app = Flask(__name__)
#CORS(app)

url = os.environ.get('CLOUDAMQP_URL', 'amqp://fxpccdrd:NJiudHhok5U_IISeM9pRqumppBFsk5Q1@wildboar.rmq.cloudamqp.com/fxpccdrd')
params = pika.URLParameters(url)
params.socket_timeout = 5

@app.route("/process", methods=['POST'])
@cross_origin()
def process():
    list_of_articles = request.get_json()
    
    return 200

    # try:s
    #     data = json.loads(request.get_json)
    # except:
    #     return 400
    # return 200
    
    # connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    # channel = connection.channel() # start a channel
    # channel.queue_declare(queue='transaction') # Declare a queue

    # channel.basic_publish(exchange='', routing_key='stockprocess', body=data)
    # print ("[x] Transaction Process sent to consumer - "+data['action']+' '+data['ticker'])
    # connection.close()

@app.after_request
def set_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Method'] = '*'
    return response


if __name__ == "__main__":
    app.run(port=5100,  debug=True)