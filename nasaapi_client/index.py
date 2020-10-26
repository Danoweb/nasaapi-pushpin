from flask import Flask, Response, request
from datetime import datetime, timedelta
import requests, os, json

app = Flask(__name__)

@app.route('/')
def index():
    resp = Response('{"message": "Client Online"}')
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/stats')
def nasa_stats():
    data = {}
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = datetime.now() - timedelta(days=-7)
    start_date = start_date.strftime('%Y-%m-%d')
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={os.environ.get('API_KEY')}"

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    api_values = json.loads(response.text)

    data = {
        "details": api_values
    }

    resp = Response(json.dumps(data))
    resp.headers['Content-Type'] = 'application/json'
    return resp 

@app.route('/stream')
def nasa_stream():
    resp = Response('')
    resp.headers['Grip-Hold'] = 'stream'
    resp.headers['Grip-Channel'] = 'nasa'
    resp.headers['Content-Type'] = 'text/plain'
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0")