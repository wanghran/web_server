from app import app, redis
from flask import render_template


@app.route('/')
def hello():
    return render_template("public/index.html", hits=redis.incr('hits'), title='Home')