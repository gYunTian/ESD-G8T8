from flask import Flask, jsonify, make_response, request
import pika, os, logging
import json
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

class DataStore():
    Name =  None
    Current = None
    Ticker = None
    Price = None
    sSentiment = None
    rsi = None
    macds = None
    macd = None
    gSentiment = None
    vix = None

data = DataStore()

#step 1
#if API takes too long, display some text
@app.route('/check/<input>')
def checker(input):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile"

    querystring = {"symbol":input}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "8a24813abdmsha86997223a2736ep1f06ffjsn810d01909dc7"
    }   

    response = requests.request("GET", url, headers=headers, params=querystring).text   
    
    if (response):
        result = json.loads(response)['quoteType']
    else:
        return "Not found!",400

    if ('longName' in result):
        #formatting
        result = result['shortName'].replace(".", " ").replace(",", " ").replace("-", " ").lower().strip().split(" ")
        remove = ["", "inc", "com", "corporation", "company", "corp", "ltd", "co", ""]
        result = [i for i in result if i not in remove]
        result = '+'.join(result)
        
        current = json.loads(response)['price']['regularMarketOpen']['raw']
        
        data.Name = result
        data.Ticker = input
        data.Current = current
    
        return {'Name': result, 'Ticker': input}, 200
    else:
        return "Not found",400

#step 2
@app.route('/initialize')
def run():
    if (data.Name and data.Ticker):
        return json.dumps({'Name': data.Name.capitalize(), 'Ticker': data.Ticker, 'Current': data.Current}), 200
    else:
        return json.dumps("No data"), 400

#step 3
@app.route('/get1')
def get1():
    #parallel 1
    #Alex stock details
    #detail = requests.get(url+ticker, headers=headers)
    return 'OKAY', 200

#step 4
@app.route('/get2')
def get2():
    #parallel 2
    #stock sentiment - ticker_news.py
    stock = requests.get('http://localhost:5006/scrape/'+data.Name, headers=headers)
    result = json.loads(stock.text)
    

    #sentiment service
    sentiment = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment = str(round(float(sentiment),2))+"%"
    data.sSentiment = sentiment
    return json.dumps({'sSentiment': sentiment}), 200

#step 5
@app.route('/get3')
def get3():
    #parallel 3
    #indicators - indicators.py
    indicators = requests.get('http://localhost:5008/indicator/'+data.Ticker, headers=headers).text
    if ('exceeded' in indicators):
        return json.dumps({'exceeded': True}), 400

    indicators = json.loads(indicators)   

    return json.dumps({'RSI': indicators['RSI'], 'MACDS': indicators['MACD_S'], 'MACD': indicators['MACD']}), 200


#step 6
@app.route('/get4')
def get4():
    #parallel 4
    #general news sentiment
    general = requests.get('http://localhost:5010/scrape', headers=headers)
    result = json.loads(general.text)
    
    #sentiment service
    sentiment = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment = str(round(float(sentiment),2))+"%"
    return json.dumps({'gSentiment': sentiment}), 200
    
#step 7
@app.route('/get5')
def get5():
    #parallel 5
    #VIX 
    vix = requests.get('http://localhost:5007/vix', headers=headers)
    result = json.loads(vix.text)
    return json.dumps({'vix': result}), 200 

#step 8
@app.route('/get6')
def get6():
    #graph div
    div = requests.get('http://localhost:5020/graph/'+data.Ticker, headers=headers)
    result = json.loads(div.text)
    return json.dumps({'data': result}), 200 

#works
# @app.route('/get7/<input>')
# def get7(input):
#     #graph div
#     item = str(input)
#     return jsonify({"name": item}), 200

@app.route('/get7', methods=['POST'])
def get7():
    #graph div
    data = json.loads(request.data)
    ticker = data['ticker']



    # url = os.environ.get('CLOUDAMQP_URL', 'amqp://fxpccdrd:NJiudHhok5U_IISeM9pRqumppBFsk5Q1@wildboar.rmq.cloudamqp.com/fxpccdrd')
    # params = pika.URLParameters(url)


    # connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    # channel = connection.channel() # start a channel
    # channel.queue_declare(queue='hello') # Declare a queue
    # #channel.queue_declare(queue='transaction', durable=True) # Declare a queue

    # channel.basic_publish(exchange='',
    #                     routing_key='hello',
    #                     body=ticker)
    # print(" [x] Sent 'Hello World!!!!!'")
    # connection.close()

    
    return request.data, 200
    
#step 9
# @app.route("/process/<asd>")
# def process(asd):
#     # url = os.environ.get('CLOUDAMQP_URL', 'amqp://fxpccdrd:NJiudHhok5U_IISeM9pRqumppBFsk5Q1@wildboar.rmq.cloudamqp.com/fxpccdrd')
#     # params = pika.URLParameters(url)
#     # params.socket_timeout = 5

    
#     data = asd.split('-')
    

#     # connection = pika.BlockingConnection(params) # Connect to CloudAMQP
#     # channel = connection.channel() # start a channel
#     # channel.queue_declare(queue='transaction') # Declare a queue

#     # channel.basic_publish(exchange='', routing_key='stockprocess', body=data)
#     # print ("[x] Transaction Process sent to consumer - "+data['action']+' '+data['ticker'])
#     # connection.close()
    
#     response = jsonify({'some': data})
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response, 200




# cors = CORS(app, resources={r"/process": {"origins": "http://localhost:port"}})

# @app.route('/process', methods=['POST', 'GET','OPTIONS'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
# def process():
#     # url = os.environ.get('CLOUDAMQP_URL', 'amqp://fxpccdrd:NJiudHhok5U_IISeM9pRqumppBFsk5Q1@wildboar.rmq.cloudamqp.com/fxpccdrd')
#     # params = pika.URLParameters(url)
#     # params.socket_timeout = 5

#     # connection = pika.BlockingConnection(params) # Connect to CloudAMQP
#     # channel = connection.channel() # start a channel
#     # channel.queue_declare(queue='transaction') # Declare a queue

#     # channel.basic_publish(exchange='', routing_key='stockprocess', body=data)
#     # print ("[x] Transaction Process sent to consumer - "+data['action']+' '+data['ticker'])
#     # connection.close()
    
#     response = jsonify({'some': 'data'}) 
#     response.header.Add("Access-Control-Allow-Origin", "*")
#     response.header.Add("Access-Control-Allow-Methods", "DELETE, POST, GET, OPTIONS")
#     response.header.Add("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")
#     return response, 200
    
# #step 9
# @app.route('/clear')
# def clear():
#     data.Name = None
#     data.Ticker = None
#     return 'Cleared', 200 
    
if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)


