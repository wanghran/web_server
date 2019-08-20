from flask import Flask

app = Flask(__name__)

from app import hello
from app import about
from app import sign_up