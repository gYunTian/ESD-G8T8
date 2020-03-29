import requests
import json
from flask import Flask
from flask_cors import CORS


#import requests
app = Flask(__name__)
CORS(app)

@app.route("/vix")
def get_vix():
    # url = "https://alpha-vantage.p.rapidapi.com/query"
    # querystring = {"datatype":"json","function":"GLOBAL_QUOTE","symbol":"VIX"}

    # headers = {
    #     'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    #     'x-rapidapi-key': "8a24813abdmsha86997223a2736ep1f06ffjsn810d01909dc7",
    #     'Content-type': "application/json"
    # }

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

    querystring = {"region":"US","symbol":"%5EVIX"}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "8a24813abdmsha86997223a2736ep1f06ffjsn810d01909dc7"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    vix = response.text 
    vix = json.loads(vix)['price']['regularMarketOpen']['raw']

    vix = json.dumps(vix, default=str)

    return vix, 200


    
if __name__ == "__main__":
    app.run(host='localhost', port=5007, debug=True)