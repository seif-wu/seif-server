from app import db

class WechatMiniProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    app_id = db.Column(db.String(255), nullable=False)
    app_secret = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<WechatMiniProgram %r>' % self.app_id
