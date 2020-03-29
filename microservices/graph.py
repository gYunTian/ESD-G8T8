import plotly
import plotly.graph_objects as go
import pandas as pd
import requests
import json
from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/graph/<ticker>')
def candlestick(ticker):
    days = '300'
    r = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/'+ticker+'?timeseries='+days)
    r = r.json()

    stockdata = r['historical']
    stockdata_df = pd.DataFrame(stockdata)

    stockdata_df['MA15'] = stockdata_df.close.rolling(15).mean()
    stockdata_df['MA50'] = stockdata_df.close.rolling(50).mean()

    data=[go.Candlestick(x=stockdata_df['date'],
    open=stockdata_df['open'],
    high=stockdata_df['high'],
    low=stockdata_df['low'],
    close=stockdata_df['close'], name="Candlesticks"), 
    go.Scatter(x=stockdata_df['date'], y=stockdata_df.MA15, line=dict(color='red', width=1), name="Fast MA"),
    go.Scatter(x=stockdata_df['date'], y=stockdata_df.MA50, line=dict(color='blue', width=1), name="Slow MA")]

    #plotly.offline.plot(data, filename='file.html')
    res = str(plotly.offline.plot(data, include_plotlyjs=False, output_type='div'))
    return json.dumps(res), 200


if __name__ == "__main__":
    app.run(host='localhost', port=5020, debug=True)