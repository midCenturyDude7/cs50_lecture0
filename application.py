from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Working with Flask and Python to develop a web application"
    return render_template("index.html", headline=headline)