from app import app
from redis import Redis
from flask import render_template

redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return render_template("public/index.html", hits=10)