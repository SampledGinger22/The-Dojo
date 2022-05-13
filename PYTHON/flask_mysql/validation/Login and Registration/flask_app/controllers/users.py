from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User

@app.route('/')
def landing():
    return redirect('/reg_login')

@app.route('/reg_login')
def reg_login():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():

    if not User.validate_user_info(request.form):
        return redirect('/reg_login')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        'first_name' : request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/reg_login')


# LOOK FOR SHIT HERE
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
    session['user_id'] = user_in_db.id
    return redirect('/success')

@app.route('/success')
def success():
    data = {
        'id': session['user_id']
    }
    user = User.get_one(data)
    return render_template('success.html', user = user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/reg_login')