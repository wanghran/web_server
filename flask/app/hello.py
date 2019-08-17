from app import app
from redis import Redis

redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return f"<h1>This Compose/Flask demo has been viewed {redis.incr('hits')} time(s)</h1>."
    # return "hello, world"