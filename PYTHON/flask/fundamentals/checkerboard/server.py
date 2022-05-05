from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def standard():
    return render_template("index.html", height = 8, number = 8, color = "red", color1 = "black")

@app.route("/<int:x>")
def heightadj(x):
    return render_template("index.html", height = x, number=8, color = "red", color1 = "black")

@app.route("/<int:x>/<int:y>")
def display(x, y):
    return render_template("index.html", height = y, number = x, color = "red", color1 = "black")

if __name__=="__main__":
    app.run(debug=True)
