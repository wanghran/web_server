from flask import Flask
from redis import Redis

app = Flask(__name__)
app.config['SECRET_KEY'] = '8a78a57658d5e78ccdfdb8ce6e0899dc'
# redis = Redis(host='localhost', port=6379)
redis = Redis(host='redis', port=6379)

from app import hello
from app import about
from app import sign_up
from app import profile