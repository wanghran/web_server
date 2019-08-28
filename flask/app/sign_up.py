from app import app
from flask import render_template, request, redirect, flash, url_for
import sys

# @app.route('/signup', methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         req = request.form
        
#         missing = []

#         for k, v in req.items():
#             if v == '':
#                 missing.append(k)
#         if missing:
#             feedback = f"missing field for {', '.join(missing)}"
#             return render_template('public/sign-up.html', feedback=feedback)

#         username = req['username']
#         email = req['email']
#         password = req['password']
#         return redirect(request.url)

#     return render_template('public/sign-up.html')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}.', 'success')
        return redirect(url_for('hello'))
    return render_template('public/register.html', title='Register', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('public/login.html', title='Login', form=form)