from marshmallow import Schema, fields


class User(Schema):
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

    avatar = fields.Str()
    username = fields.Str()
    wechat_user = fields.Nested('WechatUserSchema', exclude=("user", ))
