from marshmallow import Schema, fields
from marshmallow import EXCLUDE


class Base(Schema):
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

    class Meta:
        unknown = EXCLUDE
