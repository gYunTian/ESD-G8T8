from flask import Flask, jsonify, make_response
import json
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

class DataStore():
    Name =  None
    Ticker = None

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

        data.Name = result
        data.Ticker = input
        return {'Name': result, 'Ticker': input}, 200
    else:
        return "Not found",400

#step 2
@app.route('/initialize')
def run():
    if (data.Name and data.Ticker):
        return json.dumps({'Name': data.Name.capitalize(), 'Ticker': data.Ticker}), 200
    else:
        return json.dumps("No data"), 200

#step 3
@app.route('/get_all')
def get_all():
    #initialize json object to return
    return_arr = {
        "Stock price": "",
        "Stock sentiment": "",
        "RSI": "",
        "MACD_S": "",
        "MACD": "",
        "General sentiment": "",
        "VIX": ""
    }
    
    #parallel 1
    #Alex stock details
    #detail = requests.get(url+ticker, headers=headers)

    
    #parallel 2
    #stock sentiment - ticker_news.py
    stock = requests.get('http://localhost:5006/scrape/'+data.Name, headers=headers)
    result = json.loads(stock.text)
    

    #sentiment service
    sentiment = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment = str(round(float(sentiment),2))+"%"
    return_arr['Stock sentiment'] = sentiment


    #parallel 3
    #indicators - indicators.py
    indicators = requests.get('http://localhost:5008/indicator/'+data.Ticker, headers=headers)
    indicators = json.loads(indicators.text)
    
    return_arr["RSI"] = indicators['RSI']
    return_arr["MACD_S"] = indicators['MACD_S']
    return_arr["MACD"] = indicators['MACD']

    

    #parallel 4
    #general news sentiment
    general = requests.get('http://localhost:5010/scrape', headers=headers)
    result = json.loads(general.text)
    

    #sentiment service
    sentiment = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment = str(round(float(sentiment),2))+"%"
    return_arr['General sentiment'] = sentiment
    

    #parallel 5
    #VIX 
    vix = requests.get('http://localhost:5007/vix', headers=headers)
    result = json.loads(vix.text)
    return_arr["VIX"] = result
    
    
    #return value and status
    return return_arr, 200   


if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)


