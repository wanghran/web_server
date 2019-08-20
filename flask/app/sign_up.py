from app import app
from flask import render_template, request, redirect

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        req = request.form
        
        missing = []

        for k, v in req.items():
            if v == '':
                missing.append(k)
        if missing:
            feedback = f"missing field for {', '.join(missing)}"
            return render_template('public/sign-up.html', feedback=feedback)

        username = req['username']
        email = req['email']
        password = req['password']
        return redirect(request.url)

    return render_template('public/sign-up.html')