from . import db


class Task(db.Models):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.TextField, nullable=False)
    completed=db.Column(db.Boolean, default=False)