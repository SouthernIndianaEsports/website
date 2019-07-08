from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from database import Event
from config import db_username, db_password

app = Flask(__name__)
# TODO move this to some other type of configuraiton file like ini or yaml
app.config['SQLAlCHEMY_DATABASE_URI'] = 'mysql://{}:{}@localhost/siea'.format(db_username, db_password)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/events/<id>")
def view_event(id):
    event = Event().query.filter_by(id=id).first_or_404()
    return render_template("view_event.html", event=event)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/social")
def social():
    return render_template("social.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")
