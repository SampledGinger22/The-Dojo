from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def default():
    return redirect ("/users/new")

@app.route('/users/new')
def form():
    return render_template("form.html")

@app.route('/userspost', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template("record.html", all_users = users)

@app.route('/users/<int:id>/show')
def show(id):
    data = {
        'id':id
    }
    users = User.get_one(data)
    print(users)
    return render_template('show_user.html', user = users)

@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        'id' : id
            }
    return render_template('edit_user.html', user = User.get_one(data))

@app.route('/usersupdate/<int:id>', methods = ["POST"])
def update(id):
    data = {
        "id":id,
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.update(data)
    return redirect('/users')

@app.route('/users/<int:id>/destroy')
def delete(id):
    data = {
        'id' : id
            }
    User.delete(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)
