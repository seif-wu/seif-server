from marshmallow import Schema, fields, validate


class WechatUserSchema(Schema):
    avatar_url = fields.Str()
    name = fields.Str(validate=validate.NoneOf)
    mobile = fields.Str()
    user = fields.Nested('UserSchema', exclude=("wechat_user", ))

