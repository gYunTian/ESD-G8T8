import pika, os
import json
from flask import Flask, jsonify    
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class DataStore():
    count =  0
    queue = 0
    data = dict()

count = DataStore()

url = os.environ.get('CLOUDAMQP_URL', 'amqp://fxpccdrd:NJiudHhok5U_IISeM9pRqumppBFsk5Q1@wildboar.rmq.cloudamqp.com/fxpccdrd')
params = pika.URLParameters(url)


def callback(ch, method, properties, body):
    #data = json.loads(body)
    count.count += 1
    count.data[count.count] = json.dumps(json.loads(body))

    print(" [x] Received :" + json.dumps(json.loads(body)))
    
    if (count.count == count.queue):
        ch.stop_consuming()




@app.route('/retrieve')
def retrieve():
    count.count =  0
    count.queue = 0
    count.data = dict()

    element = ""
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    resp = channel.queue_declare(queue='esd', durable=True)

    channel.basic_consume(queue='esd', on_message_callback=callback, auto_ack=True)

    count.queue = resp.method.message_count

    if (count.queue < 1):
        channel.stop_consuming()
        print('No message in queue')
        return {'status': 'No message in queue'}, 200
    
    channel.start_consuming()
    
    print(count.data)
    for key, value in count.data.items():
        value = json.loads(value)
        element += '<tr>\
        <td><input type="checkbox" id="'+str(value['unique'])+'" class="larger"></td>\
        <td>Username</td>\
        <td>'+str(value['ticker'])+'</td>\
        <td>'+str(value['amt'])+'</td>\
        <td>'+str(value['current'])+'</td>\
        <td>'+str(value['action'])+'</td>\
        </tr>'
    
    #return in json format
    return {'status' : 'retrieved', 'data': element}, 200
    

if __name__ == "__main__":
    app.run(host='localhost', port=5500, debug=True)
