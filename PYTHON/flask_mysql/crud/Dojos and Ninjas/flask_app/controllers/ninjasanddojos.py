from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def default():
    return redirect ("/dojos")

@app.route('/dojos')
def form_newdojo():
    dojo = Dojo.get_all()
    return render_template("dojos.html", dojos = dojo)

@app.route('/dojospost', methods=["POST"])
def dojopost():
    data = {
        "name": request.form["name"],
    }
    Dojo.save_dojo(data)
    return redirect('/dojos')

@app.route('/dojoroster/<int:id>')
def dojoroster(id):
    data = {
        "id":id
    }
    dojo = Dojo.get_one(data)
    ninja = Ninja.get_all_ninjas(data)
    return render_template ("dojoroster.html", dojo = dojo, ninja = ninja)

@app.route('/newninja')
def form_newninja():
    dojo = Dojo.get_all()
    return render_template("newninja.html", dojos = dojo)

@app.route('/ninjapost', methods=["POST"])
def ninjapost():
    data = {
        "id":id,
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }
    Dojo.save_ninja(data)
    return redirect('/dojos')