from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'user_account'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, primary_key=True)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email
