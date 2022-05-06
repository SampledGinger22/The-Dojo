from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "hellothere"

@app.route('/')
def refreshcounter():
    if "visits" in session:
        session["visits"] += 1
    else: 
        session["visits"] = 1
    return render_template("index.html")

@app.route("/count_up")
def count():
    return redirect("/")

@app.route("/destroy_session")
def clear():
    session.pop("visits")
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)