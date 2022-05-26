from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User
from flask_app.models.customer import Customer
from flask_app.models.project import Project
from flask_app.models.contact import Contact

@app.route('/')
def landing():
    return redirect('/login')

@app.route('/login')
def login():
    if "user_id" in session:
        return redirect('/dashboard')
    return render_template('main_login.html')

@app.route('/login/commit', methods=['POST'])
def commit_login():
    data = {
        'email':request.form['email'],
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Incorrect email or password')
        return redirect('/login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Incorrect email or password')
        return redirect('/login')
    if not User.validate_login(request.form):
        return redirect('/login')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/register')
def register():
    return render_template('main_registration.html')

@app.route('/register/commit', methods=['POST'])
def submit_registration():
    print(request.form)
    if not User.validate(request.form):
        return redirect('/register')
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
        return redirect('/login')
    data = {
        'user_id': session['user_id'],
    }
    context = {
        'customers': Customer.get_all(data),
        'projects': Project.get_all(data),
        'primaries': Contact.get_primary()
    }
    return render_template('dash_user.html', **context)

@app.route('/user/profile/')
def user_profile(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'user_id': session['user_id']
    }
    context = {
        "user": User.get_one(data)
    }
    return render_template('view_profile.html', **context)

@app.route('/user/profile/edit')
def edit_user():
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'user_id': session['user_id']
    }
    context = {
        "user": User.get_one(data)
    }
    return render_template('edit_profile.html', **context)

@app.route('/user/profile/edit/commit', methods=['POST'])
def submit_user_changes():
    data = {
        **request.form,
        'user_id' : session['user_id']
    }
    if not User.validate(request.form):
        return redirect('/user/profile/edit')
    User.update(data)
    return redirect('/user/profile')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')