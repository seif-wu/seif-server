from marshmallow import Schema, fields


class WechatUserSchema(Schema):
    id = fields.Int(dump_only=True)
    avatar_url = fields.Str()
    name = fields.Str()
    mobile = fields.Str()
    user = fields.Nested('UserSchema', exclude=("wechat_user", ))
