from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return f"This Compose/Flask demo has been viewed {redis.incr('hits')} time(s)."
    # return "hello, world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)