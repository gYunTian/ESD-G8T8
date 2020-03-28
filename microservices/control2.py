from flask import Flask, jsonify, make_response
import json
from flask_cors import CORS
import requests

app = Flask(__name__)

@app.route('/get/general')
def get_general():
    #VIX, general sentiment
    #done
    #need parallel
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    #initialize json to return
    return_arr = {
        "General sentiment": "",
        "VIX": ""
    }
    
    #parallel 1
    #general news sentiment
    general = requests.get('http://localhost:5003/scrape', headers=headers)
    result = json.loads(general.text)
    

    #sentiment service
    sentiment = requests.post('http://localhost:5004/sentiment', json=result, headers=headers).text
    sentiment = str(round(float(sentiment),2))+"%"
    return_arr['General sentiment'] = sentiment

    
    #VIX 
    vix = requests.get('http://localhost:5007/vix', headers=headers)
    result = json.loads(vix.text)
    return_arr["VIX"] = result


    #return result json
    return return_arr, 200   

    
    #lcaolhost:5005/get/ticker
if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)


