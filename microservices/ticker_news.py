import requests
import json
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS


#import requests
app = Flask(__name__)
CORS(app)

#stock news scraper
@app.route("/scrape/<name>")
def scrape_stock_news(name):
    
    #set up dict for two apis
    url = 'https://www.cityfalcon.com/webapi/v1/search/metadata/stories?api_key=Fma36p9juaU2qGTLUiEDpw&categories=mp,op,r&order_by=top&time_filter=day1&languages=en,de,es,fr,pt&min_score=1&all_languages=false&query=%22%5C%22group:Topic:101:Ford+Motor%5C%22%22&limit=30'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser').text
    parsed = json.loads(soup)
    stories = parsed['stories']
    
    return_str = ""
    for item in stories:
        return_str += item['title']+'~'
    return_str = return_str[:-1]
    
    return json.dumps(return_str), 200
    
if __name__ == "__main__":
    app.run(host='localhost', port=5006, debug=True)
    