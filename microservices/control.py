from flask import Flask, jsonify, make_response
import json
from flask_cors import CORS
import requests

app = Flask(__name__)


@app.route('/get/<string:ticker>')
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
    #stock sentiment - ticker_news.py
    stock = requests.get('http://localhost:5006/scrape/'+ticker, headers=headers)
    result = json.loads(stock.text)
    

    #sentiment service
    sentiment = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment = str(round(float(sentiment),2))+"%"
    return_arr['Stock sentiment'] = sentiment
    return return_arr, 200

    #parallel 3
    #indicators - indicators.py
    indicators = requests.get('http://localhost:5008/indicator/'+ticker, headers=headers)
    indicators = json.loads(indicators.text)
    
    return_arr["RSI"] = indicators['RSI']
    return_arr["MACD_S"] = indicators['MACD_S']
    return_arr["MACD"] = indicators['MACD']

    #return value and status
    return return_arr, 200   

    
if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)


