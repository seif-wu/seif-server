from app import db
from .base import Base


class WorkHistory(db.Model, Base):
    company_name = db.Column(db.String(128), nullable=False)
    time_period = db.Column(db.String(128), nullable=False)
    jobs = db.Column(db.String(255))
    desc = db.Column(db.Text)
    personal_information_id = db.Column(
        db.Integer, db.ForeignKey('personal_information.id'))
