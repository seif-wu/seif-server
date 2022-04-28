from datetime import datetime
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from app import db
from app.models.schema.watched_schema import WatchedSchema
from app.models.watched import Watched

weapp_watched_bp = Blueprint('watched', __name__, url_prefix='/watched')


@weapp_watched_bp.get('')
@jwt_required()
def index():
    args = request.args
    watcheds = Watched.query.paginate(page=args.get(
        "page", 1), per_page=args.get("pageSize", 10))
    watched_schema = WatchedSchema()
    result = watched_schema.dump(watcheds.items, many=True)

    return jsonify(
        success=True,
        date=result,
        meta={
            "has_next": watcheds.has_next,
            "has_prev": watcheds.has_prev,
            "page": watcheds.page,
            "total": watcheds.total,
        }
    )


@weapp_watched_bp.post('')
@jwt_required()
def create():
    current_user_id = get_jwt_identity()

    w = Watched.query.filter_by(tmdb_id=request.json.get(
        "tmdb_id"), user_id=current_user_id).first()
    if w is not None:
        return jsonify(
            success=False,
            message="已存在于列表中"
        ), 400

    watched = Watched(
        title=request.json.get("title"),
        tmdb_id=request.json.get("tmdb_id"),
        poster_url=request.json.get("poster_url"),
        backdrop_path=request.json.get("backdrop_path"),
        media_type=request.json.get("media_type"),
        watched_at=datetime.now(),
        user_id=current_user_id,
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


@weapp_watched_bp.get('<int:id>')
@jwt_required()
def show(id):
    w = Watched.query.get(id)
    if w is None:
        return jsonify(
            success=False,
            message="资源不存在",
        ), 404

    watched_schema = WatchedSchema()
    result = watched_schema.dump(w)

    return jsonify(
        success=True,
        data=result
    )

@weapp_watched_bp.delete('<int:id>')
@jwt_required()
def destroy(id):
    w = Watched.query.get(id)
    if w is None:
        return jsonify(
            success=False,
            message="资源不存在",
        ), 404

    db.session.delete(w)
    db.session.commit()

    return jsonify(
        success=True,
        message="删除成功"
    )
