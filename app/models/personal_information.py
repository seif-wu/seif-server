from app import db
from .base import Base

class PersonalInformation(db.Model, Base):
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer)
    mobile = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(128))
    num_projects = db.Column(db.Integer)
    work_experience = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    educational_background = db.Column(db.String(128))
    desc = db.Column(db.Text)

    @staticmethod
    def myself():
        return PersonalInformation.query.first()
