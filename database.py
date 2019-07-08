from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Event(db.Model):
    __tablename__ = "Events"
