from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def default():
    return redirect ("/dojos")

@app.route('/dojos')
def form():
    dojo = Dojo.get_all()
    return render_template("dojos.html", dojo = dojo)

@app.route('/dojospost', methods=["POST"])
def create_user():
    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojoroster/<int:id>')
def default(id):
    data = {
        "id":id
    }
    dojo = Dojo.get_one(data)
    ninja = Ninja.get_all_ninjas(data)
    return render_template ("dojoroster.html", dojo = dojo, ninja = ninja)