from app import db


class WantWatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    tmdb_id = db.Column(db.String(255), nullable=False)
    poster_url = db.Column(db.Text)
    backdrop_path = db.Column(db.Text)
    media_type = db.Column(db.String(32))
    watched_at = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
