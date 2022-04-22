from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
import requests
import secrets

from app import db
from app.models.wechat_mini_program import WechatMiniProgram
from app.models.wechat_user import WechatUser
from app.models.user import User

weapp_auth_bp = Blueprint('weapp_auth', __name__, url_prefix='/auth')


@weapp_auth_bp.post('')
def auth():
    weapp = WechatMiniProgram.default()

    if weapp is None:
        return jsonify({
            "success": False,
            "message": "小程序配置错误",
        }), 400

    jscode2session_params = {
        'appid': weapp.app_id,
        'secret': weapp.app_secret,
        'js_code': request.json.get("js_code"),
        'grant_type': 'authorization_code',
    }

    res = requests.get(
        'https://api.weixin.qq.com/sns/jscode2session', params=jscode2session_params)

    if res.json().get('errcode') is not None:
        return jsonify({
            "success": False,
            "message": "获取 Session 错误",
        }), 400

    wechat_openid = res.json().get('openid')
    avatar = request.json.get('avatar_url')
    name = request.json.get('name')

    wechat_user = WechatUser.query.filter_by(
        wechat_openid=wechat_openid).first()

    user = None
    if wechat_user is None:
        u = User(avatar=avatar, username=wechat_openid,
                 password=secrets.token_hex(16))
        w = WechatUser(name=name, wechat_openid=wechat_openid,
                       avatar_url=avatar, user=u)
        db.session.add(u)
        db.session.add(w)
        db.session.commit()

        user = u
    else:
        wechat_user.name = name
        wechat_user.avatar_url = avatar
        user = wechat_user.user
        db.session.commit()

    access_token = create_access_token(identity=user)
    return jsonify({
        "success": True,
        "access_token": access_token
    }), 200
