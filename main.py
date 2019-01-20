from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from navigation import navigation_init

app = Flask(__name__)
Bootstrap(app)

navigation_init(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/about")
def about():
    return render_template("about.html")
