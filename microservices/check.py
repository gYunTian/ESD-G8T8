from flask import Flask, jsonify, make_response
import json
from flask_cors import CORS
import requests
import yfinance as yf

app = Flask(__name__)
CORS(app)

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

            
        
        # general = requests.get('http://localhost:5006/scrape/'+result, headers=headers)
        # result = json.loads(general.text)

        # sentiment = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
        # return_arr = {
        #     'Stock sentiment': ''
        # }   
        # sentiment = str(round(float(sentiment),2))+"%"

        # return_arr = {
        #     'Stock sentiment': ''
        # }
        
        # return_arr['Stock sentiment'] = sentiment
        return {'Name': result}, 200
    else:
        return "Not found",400

if __name__ == "__main__":
    app.run(host='localhost', port=5010, debug=True)


