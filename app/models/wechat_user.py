from app import db


class WechatUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    mobile = db.Column(db.String(20), nullable=False)
    avatar_url = db.Column(db.String(255))
    wechat_userid = db.Column(db.String(255))
    wechat_openid = db.Column(db.String(255))
    wechat_unionid = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", back_populates="wechat_user")

    def __repr__(self):
        return '<WechatUser %r>' % self.name
