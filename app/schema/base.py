from marshmallow import Schema, fields
from marshmallow import EXCLUDE


class Base(Schema):
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)

    class Meta:
        unknown = EXCLUDE
