from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask WebAPI</h1>"

@app.route('/ping')
def pinger():
    return {'message':'Hello there!!'} 