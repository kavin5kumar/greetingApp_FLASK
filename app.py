from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "123@kav@453@Kmu"

@app.route('/')
def index():
  flash("What's your Name?")
  return render_template("index.html")

@app.route('/greet', methods=["POST", "GET"])
def greet():
  flash("HI " + str(request.form['name_in']) + ", Great to see YOU!!!")
  return render_template("index.html")


