from flask import Flask,render_template,request, flash, session, redirect
import re
app = Flask(__name__)
app.secret_key = "twinjuan"

NAME_REGEX = re.compile(r'^(?=.*[0-9]).+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z]).{9,}$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if len(request.form['first_name']) < 1:
        flash("First Name cannot be blank!")
        return redirect("/")
    elif NAME_REGEX.match(request.form['first_name']):
        flash("Invalid First Name!")
        return redirect("/")

    if len(request.form['last_name']) < 1:
        flash("Last Name cannot be blank!")
        return redirect("/")
    elif NAME_REGEX.match(request.form['last_name']):
        flash("Invalid Last Name!")
        return redirect("/")

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect("/")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect("/")

    if len(request.form['password']) < 1:
        flash("Password cannot be blank!")
        return redirect("/")
    elif len(request.form['confirmed']) < 1:
        flash("Confirmed Password cannot be blank!")
        return redirect("/")
    elif request.form['confirmed'] != request.form['password']:
        flash("Passwords dont match!")
        return redirect("/")
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash("Invalid Password!")
        return redirect("/")
        
    return redirect("/")

app.run(debug=True)