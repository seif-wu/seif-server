import os
import base64
import requests
from flask import Blueprint
from flask import jsonify

github_user_bp = Blueprint('github_user_bp', __name__, url_prefix='/user')


@github_user_bp.get('')
def user():
    # TODO GitHub 用户名可配置
    url = "https://api.github.com/users/seif-wu"

    basic_token = base64.b64encode(
        bytes(f"seif-wu:{os.getenv('GITHUB_TOKEN')}", 'utf-8'))
    headers = {
        'Authorization': f"Basic {basic_token}",
        'Content-Type': 'application/json'
    }

    resp = requests.request("GET", url, headers=headers)

    return jsonify({
        "success": True,
        "data": resp.json(),
    })
