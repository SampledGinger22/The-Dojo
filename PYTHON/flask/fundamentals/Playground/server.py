from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def index():
    return render_template("index.html", phrase="hello", times=5)  

@app.route("/hello/<string:banana>/<int:num>")
def hello(banana,num):
    return render_template("hello.html",banana=banana,num=num)
if __name__=="__main__":
    app.run(debug=True)                   

