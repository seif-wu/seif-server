from marshmallow import Schema, fields


class WorkHistorySchema(Schema):
    id = fields.Int(dump_only=True)
    desc = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    company_name = fields.Str()
    time_period = fields.Str()
    jobs = fields.Str()
    personal_information_id = fields.Int()
    personal_information = fields.Nested(
        'PersonalInformationSchema', exclude=("work_histories", ))
