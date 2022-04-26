from app import db


class Watched(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    tmdb_id = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.Text)
    meida_type = db.Column(db.String(32))
    watched_at = db.Column(db.DateTime)
