from .db import db

class Note(db.Document):
    whom = db.StringField(required=True)
    poop = db.IntField(required=True, min_value=0, max_value=7)
    barked = db.BooleanField(required=True)
    reasonForBark = db.StringField(required=True)
    desc = db.StringField(required=True)

