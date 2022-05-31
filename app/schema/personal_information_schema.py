from marshmallow import Schema, fields

class PersonalInformationSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    age = fields.Int()
    mobile = fields.Str()
    email = fields.Str()
    num_projects = fields.Int()
    work_experience = fields.Int()
    educational_background = fields.Str()
    desc= fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
