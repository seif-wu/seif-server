from datetime import datetime
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from app import db
from app.models.schema.want_watch_schema import WantWatchSchema
from app.models.want_watch import WantWatch

weapp_want_watched_bp = Blueprint(
    'want_watch', __name__, url_prefix='/want_watch')

@weapp_want_watched_bp.get('')
@jwt_required()
def index():
    args = request.args
    want_watches = WantWatch.query.paginate(page=args.get(
        "page", 1), per_page=args.get("pageSize", 10))
    want_watche_schema = WantWatchSchema()
    result = want_watche_schema.dump(want_watches.items, many=True)

    return jsonify(
        success=True,
        date=result,
        meta={
            "has_next": want_watches.has_next,
            "has_prev": want_watches.has_prev,
            "page": want_watches.page,
            "total": want_watches.total,
        }
    )


@weapp_want_watched_bp.post('')
@jwt_required()
def create():
    current_user_id = get_jwt_identity()

    w = WantWatch.query.filter_by(tmdb_id=request.json.get(
        "tmdb_id"), user_id=current_user_id).first()
    if w is not None:
        return jsonify(
            success=False,
            message="已存在于列表中"
        ), 400

    want_watch = WantWatch(
        title=request.json.get("title"),
        tmdb_id=request.json.get("tmdb_id"),
        poster_url=request.json.get("poster_url"),
        backdrop_path=request.json.get("backdrop_path"),
        media_type=request.json.get("media_type"),
        watched_at=datetime.now(),
        user_id=current_user_id,
    )

    db.session.add(want_watch)
    db.session.commit()

    watched_schema = WantWatchSchema()
    result = watched_schema.dump(want_watch)

    return jsonify(
        success=True,
        message="创建成功",
        data=result,
    ), 200


@weapp_want_watched_bp.delete('<int:id>')
@jwt_required()
def destroy(id):
    w = WantWatch.query.get(id)
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

@weapp_want_watched_bp.get('<int:id>')
@jwt_required()
def show(id):
    w = WantWatch.query.get(id)
    if w is None:
        return jsonify(
            success=False,
            message="资源不存在",
        ), 404

    schema = WantWatchSchema()
    result = schema.dump(w)

    return jsonify(
        success=True,
        data=result
    )
