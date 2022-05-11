from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/tableresults')

@app.route('/tableresults')
def index():
    users = User.get_all()
    print(users)
    return render_template("record.html", all_users = users)

if __name__ == "__main__":
    app.run(debug=True)
