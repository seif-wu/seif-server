from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from app.models.schema.wechat_user_schema import WechatUserSchema
from app.models.user import User


weapp_user_bp = Blueprint('weapp_user', __name__, url_prefix='/user')


@weapp_user_bp.get('')
@jwt_required()
def current_user():
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)
    wechat_user_schema = WechatUserSchema()
    result = wechat_user_schema.dump(user.wechat_user)

    return jsonify(
      success=True,
      data=result,
    ), 200
