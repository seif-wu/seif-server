from app import db
from .base import Base

class WechatMiniProgram(db.Model, Base):
    name = db.Column(db.String(128), nullable=False)
    app_id = db.Column(db.String(255), nullable=False)
    app_secret = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<WechatMiniProgram %r>' % self.app_id

    @staticmethod
    def default():
        return WechatMiniProgram.query.filter_by(name='default').first()
