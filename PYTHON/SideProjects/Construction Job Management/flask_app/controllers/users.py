from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User

@app.route('/')
def landing():
    return redirect('/login')

@app.route('/login')
def login():
    if "user_id" in session:
        return redirect('/dashboard')
    return render_template('login.html')

@app.route('/login/commit', methods=['POST'])
def commit_login():
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
    if not User.validate_user_info(request.form):
        return redirect('/login')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/register/commit', methods=['POST'])
def submit_registration():

    if not User.validate_user_info(request.form):
        return redirect('/login')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        **request.form,
        'password': pw_hash
    }
    User.save(data)
    return redirect('/login')

@app.route('/dashboard')
def success():
    if "user_id" not in session:
        return redirect('/reg_login')
    data = {
        'id': session['user_id']
    }
    context = {
        "user": User.get_one_user(data)
    }
    user_id = session['user_id']
    return render_template('dashboard.html', **context, user_id = user_id)

@app.route('/user/profile/')
def user_profile(id):
    data = {
        'user_id': session['user_id']
    }
    context = {
        "user": User.get_one_user(data)
    }
    return render_template('user_profile.html', **context)

@app.route('/user/profile/edit')
def edit_user():
    data = {
        'user_id': session['user_id']
    }
    context = {
        "user": User.get_one_user(data)
    }
    return render_template('edit_profile.html', **context)

@app.route('user/profile/edit/commit')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')