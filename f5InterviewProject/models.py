from datetime import datetime
from f5InterviewProject import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=True)
    lastName = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Post('{self.firstName}', '{self.lastName}')"