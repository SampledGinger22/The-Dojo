from unicodedata import name
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "hellothere"

@app.route('/')
def displayform():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    session["name"] = "full_name"
    session["location"] = "fav_location"
    session["language"] = "fav_language"
    session["comment"] = "comments"
    print(request.form["full_name"])
    return redirect("/")

@app.route("/results")
def results():
    return render_template("return.html")

if __name__=="__main__":
    app.run(debug=True)