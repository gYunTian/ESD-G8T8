from flask import Flask, jsonify, make_response
import json
from flask_cors import CORS
import requests

app = Flask(__name__)


@app.route('/get/<string: ticker>')
def send_ticker(ticker):
    #should only orchestrate for Alex's, stock news, indicator

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    #initialize json object to return
    return_arr = {
        "Stock price": "",
        "Stock sentiment": "",
        "RSI": "",
        "MACD_S": "",
        "MACD": ""
    }
    
    #parallel 1
    #Alex stock details
    #detail = requests.get(url+ticker, headers=headers)


    #parallel 2
    #stock sentiment
    stock = requests.get('http://localhost:5006/scrape/'+ticker, headers=headers)
    result = json.loads(stock.text)
    
    sentiment = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment += str(round(float(sentiment),2))+"%"
    
    return_arr["Stock sentiment"] = sentiment
    
    #parallel 3
    #indicators
    indicators = requests.get('http://localhost:5007/vix', headers=headers)
    indicators = json.loads(indicators.text)
    #rsi = indicators['RSI']
    #macds = indicators['MACD_S']
    #macd = indicators['MACD']
    #return_arr["VIX"] = rsi
    #return_arr["VIX"] = macds
    #return_arr["VIX"] = macd

    #return value and status
    return indicators, 200   

    
if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)


