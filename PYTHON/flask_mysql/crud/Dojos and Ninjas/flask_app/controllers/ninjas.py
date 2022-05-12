from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja

@app.route('/newninja')
def form():
    return render_template("newninja.html")

@app.route('/ninjapost', methods=["POST"])
def create_user():
    data = {
        "dojo_id" : request.form["dojo_id"],
        "first_name": request.form["full_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }
    Ninja.save(data)
    return redirect('/dojos')