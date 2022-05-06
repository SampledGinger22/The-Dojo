from unicodedata import name
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "hellothere"

@app.route('/')
def displayform():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    session["name"] = request.form["full_name"]
    session["location"] = request.form["dojo_location"]
    session["language"] = request.form["fav_language"]
    session["comment"] = request.form["comments"]
    return redirect("/results")

@app.route("/results")
def results():
    return render_template("return.html")

if __name__=="__main__":
    app.run(debug=True)