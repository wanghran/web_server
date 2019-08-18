from app import app

@app.route('/about')
def about():
    return "<h1>First test on webserver with flask</h1>."