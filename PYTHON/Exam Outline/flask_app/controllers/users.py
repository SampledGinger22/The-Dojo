from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/')
def landing():
    return redirect('/reg_login')

@app.route('/reg_login')
def reg_login():
    if "user_id" in session:
        return redirect('/user_dash')
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():

    if not User.validate_user_info(request.form):
        return redirect('/reg_login')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        **request.form,
        'password': pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/reg_login')

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email':request.form['email'],
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Incorrect email or password')
        return redirect('/reg_login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Incorrect email or password')
        return redirect('/reg_login')
    if not User.email_exist(request.form):
        return redirect('/reg_login')
    session['user_id'] = user_in_db.id
    return redirect('/user_dash')

@app.route('/user_dash')
def success():
    if "user_id" not in session:
        return redirect('/reg_login')
    data = {
        'id': session['user_id']
    }
    context = {
        "user": User.get_one(data)
    }
    return render_template('user_dash.html', **context)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/reg_login')