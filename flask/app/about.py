from app import app
from flask import render_template
from datetime import datetime

my_name = 'Haoran'

my_age = 24

languages = ['Python', 'Java', 'C++', 'C']
date = datetime.today()

def repeat(x, times=1):
    return x*times

suspicious = "<script>alert('NEVER TRUST USER INPUT!')</script>"

@app.template_filter("clean_date")
def clean_date(date):
    return date.strftime("%b %d %Y")

@app.route('/about')
def about():
    return render_template("public/about.html", my_name='Haoran', my_age=my_age, languages=languages,
                           repeat=repeat, date=date, suspicious=suspicious)