from app import app
from redis import Redis
from flask import render_template
import json

# redis = Redis(host='localhost', port=6379)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return render_template("public/index.html", hits=redis.incr('hits'), title='Home')

@app.route('/profile/<username>')
def profile(username):
    users_json = redis.get('users')
    users = json.loads(users_json)

    user = None
    if username in users:
        user = users[username]
    return render_template('public/dynamic.html', user=user, username=username)