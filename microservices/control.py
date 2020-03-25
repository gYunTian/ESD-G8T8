from flask import Flask, jsonify, make_response
import json
from flask_cors import CORS
import requests
app = Flask(__name__)


@app.route('/get')
def get_articles():
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    ticker = 'AAPL'

    #parallel 1
    #general sentiment
    general = requests.get('http://localhost:5003/scrape', headers=headers)
    result = json.loads(general.text)
    
    #sentiment service
    sentiment = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment = str(round(float(sentiment),2))+"%"
    


    #stock sentiment
    stock = requests.get('http://localhost:5006/scrape/'+ticker, headers=headers)
    result = json.loads(stock.text)
    
    sentiment2 = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment2 += str(round(float(sentiment2),2))+"%"
    
    #return value and status
    return json.dumps(result), 200   

    

if __name__ == "__main__":
    app.run(host='localhost', port=5005, debug=True)


