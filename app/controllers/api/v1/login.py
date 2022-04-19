
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from app.models.user import User

login_bp = Blueprint('login', __name__, url_prefix='/login')


@login_bp.route("", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(username=username).one_or_none()
    print( user, username)

    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401

    # Notice that we are passing in the actual sqlalchemy user object here
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)