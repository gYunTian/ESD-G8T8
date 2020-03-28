import requests
import json
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS

#import requests
app = Flask(__name__)
CORS(app)

@app.route("/scrape")
def scrape_stories():
    url = 'https://www.cityfalcon.com/webapi/v1/stories?categories=mp,op,r&order_by=top&time_filter=day1&languages=en,de,es,fr,pt&min_score=1&asset_classes=163&twitter_following_only=false&with_links=false&all_languages=false&premium_only=false'
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
    app.run(host='localhost', port=5003, debug=True)
    