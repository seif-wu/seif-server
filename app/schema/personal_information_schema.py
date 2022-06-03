from marshmallow import Schema, fields


class PersonalInformationSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    age = fields.Int()
    mobile = fields.Str()
    email = fields.Str()
    num_projects = fields.Int()
    work_experience = fields.Int()
    birthday = fields.Date()
    educational_background = fields.Str()
    desc = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    other_info = fields.Str()
    work_histories = fields.List(fields.Nested(
        'WorkHistorySchema', exclude=("personal_information", )))
    project_histories = fields.List(fields.Nested(
        'ProjectHistorySchema', exclude=("personal_information", )))
