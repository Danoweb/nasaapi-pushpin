from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '{"message": "TackerGG Client Online"}'

@app.route('/player-stats')
def player_stats(params):
    return '{"details":"{}"}'

