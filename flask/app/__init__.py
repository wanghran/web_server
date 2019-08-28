from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '8a78a57658d5e78ccdfdb8ce6e0899dc'

from app import hello
from app import about
from app import sign_up