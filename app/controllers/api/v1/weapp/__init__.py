# 微信小程序相关接口
from flask import Blueprint

from .auth import weapp_auth_bp
from .user import weapp_user_bp


weapp_bp = Blueprint('weapp', __name__, url_prefix='/weapp')

weapp_bp.register_blueprint(weapp_auth_bp)
weapp_bp.register_blueprint(weapp_user_bp)
