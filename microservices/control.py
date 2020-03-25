from flask import Flask, jsonify, make_response
import json
from flask_cors import CORS
import requests
app = Flask(__name__)


@app.route('/get/<ticker>')
def get_articles(ticker):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    ticker = 'AAPL'
    
    #initialize json to return
    return_arr = {
        "Stock price": "",
        "General sentiment": "",
        "Stock sentiment": "",
        "VIX": "",
        "RSI": "",
        "MACD_S": "",
        "MACD": ""
    }
    
    #Alex stock details
    #detail = requests.get(url, headers=headers)




    #parallel 1
    #general news sentiment
    general = requests.get('http://localhost:5003/scrape', headers=headers)
    result = json.loads(general.text)
    
    #sentiment service
    sentiment = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment = str(round(float(sentiment),2))+"%"
    
    return_arr["General sentiment"] = sentiment

    
    #stock sentiment
    stock = requests.get('http://localhost:5006/scrape/'+ticker, headers=headers)
    result = json.loads(stock.text)
    
    sentiment2 = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment2 += str(round(float(sentiment2),2))+"%"
    
    return_arr["Stock sentiment"] = sentiment2
    

    #VIX 
    vix = requests.get('http://localhost:5007/vix', headers=headers)
    result = json.loads(vix.text)
    return_arr["VIX"] = result

    
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

    
    #lcaolhost:5005/get/ticker
if __name__ == "__main__":
    app.run(host='localhost', port=5005, debug=True)


