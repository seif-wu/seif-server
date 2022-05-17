import requests
from flask import Blueprint
from flask import jsonify

github_user_bp = Blueprint('github_user_bp', __name__, url_prefix='/user')


@github_user_bp.get('')
def user():
    # TODO GitHub 用户名可配置
    url = "https://api.github.com/users/seif-wu"
    resp = requests.request("GET", url)

    return jsonify({
        "success": True,
        "data": resp.json(),
    })
