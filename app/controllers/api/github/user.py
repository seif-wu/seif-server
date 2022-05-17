from flask import Blueprint, jsonify, request

github_user_bp = Blueprint('github_user_bp', __name__, url_prefix='/user')


@github_user_bp.get('')
def user():
    pass
