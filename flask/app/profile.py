from app import app, redis
from flask import render_template
import json

@app.route('/profile/<username>')
def profile(username):
    users_json = redis.get('users')
    users = json.loads(users_json)

    user = None
    if username in users:
        user = users[username]
    return render_template('public/dynamic.html', user=user, username=username)