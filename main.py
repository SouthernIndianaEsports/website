from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/social")
def social():
    return render_template("social.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")
