from flask import Flask
from redis import Redis
from flask_sqlalchemy import SQLAlchemy

POSTGRES = {
    'user': 'user',
    'pw': 'pass',
    'db': 'test',
    'host': 'localhost',
    'port': '5432',
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8a78a57658d5e78ccdfdb8ce6e0899dc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s\
@%(host)s:%(port)s/%(db)s' % POSTGRES
redis = Redis(host='localhost', port=6379)
# redis = Redis(host='redis', port=6379)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


from app import hello
from app import about
from app import sign_up
from app import profile