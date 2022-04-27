from datetime import datetime
from email import message
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from app import db
from app.models.schema.watched_schema import WatchedSchema
from app.models.watched import Watched

weapp_watched_bp = Blueprint('watched', __name__, url_prefix='/watched')


@weapp_watched_bp.post('')
@jwt_required()
def create():
    current_user_id = get_jwt_identity()

    w = Watched.query.filter_by(tmdb_id = request.json.get("tmdb_id"), user_id = current_user_id).first()
    if w is not None:
        return jsonify(
          success=False,
          message="已存在于列表中"
        ), 400

    watched = Watched(
        title = request.json.get("title"),
        tmdb_id = request.json.get("tmdb_id"),
        poster_url = request.json.get("poster_url"),
        backdrop_path = request.json.get("backdrop_path"),
        media_type = request.json.get("media_type"),
        watched_at = datetime.now(),
        user_id = current_user_id,
    )

    db.session.add(watched)
    db.session.commit()

    watched_schema = WatchedSchema()
    result = watched_schema.dump(watched)


    return jsonify(
      success=True,
      message="创建成功",
      data=result,
    ), 200
