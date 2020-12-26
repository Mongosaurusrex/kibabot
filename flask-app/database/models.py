from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Note(db.Document):
    whom = db.StringField(required=True)
    poop = db.IntField(required=True, min_value=0, max_value=7)
    barked = db.BooleanField(required=True)
    reasonForBark = db.StringField(required=True)
    desc = db.StringField(required=True)

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)