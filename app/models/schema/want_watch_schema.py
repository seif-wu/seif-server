

from marshmallow import Schema, fields

class WantWatchSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    tmdb_id = fields.Str()
    poster_url = fields.Str()
    backdrop_path = fields.Str()
    meida_type = fields.Str()
    watched_at = fields.DateTime()