from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Flask, jsonify, request
import json
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/sentiment", methods=['POST'])
def getSentiment():
    list_of_articles = request.get_json().split(",")
    
    sia = SentimentIntensityAnalyzer()
    result = {'p':0, 'neg':0, 'neu':0}
    overall = {'p':0, 'neg':0, 'neu':0}
    
    for article in list_of_articles:
        sentiment_dict = sia.polarity_scores(article)
        score = sentiment_dict['compound'] * 100

        if score >= 0.05 : 
            result['p'] += 1
            overall['p'] += score

        elif score <= - 0.05 : 
            result['neg'] += 1
            overall['neg'] += score

        else : 
            result['neu'] += 1
            overall['neu'] += score
    max_count = max(result, key=result.get)
    

    #check if same count
    check_array = []
    for key in result:
        if (key == max_count):
            check = result[key] #store value of the max count (pos, neg, neu)
            check_array.append(key)
        
    for key in result:
        if (key != max_count):
            if (check == result[key]): #if same count as max counted sentiment
                check_array.append(key)
    
    #if same same number of sentiments
    if (len(check_array) > 1):
        high = 0
        for item in check_array:
            if ((overall[item]/check > high or overall[item]/check < high) and overall[item] != 0): #get average
                high = overall[item]/check
                use = item #get the highest sentiment average
        average = str(overall[use]/result[use])+"%"

    else:
        average = str(overall[max_count]/result[max_count])
    
    return average, 200
    

if __name__ == "__main__":
    app.run(host='localhost', port=5004, debug=True)