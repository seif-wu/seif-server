import json
from sqlalchemy import func
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from app.models.watched import Watched


stats_bp = Blueprint('stats', __name__, url_prefix='/stats')


@stats_bp.get("/watched")
@jwt_required()
def watched():
    current_user_id = get_jwt_identity()

    w = Watched.query.filter_by(
        user_id=current_user_id
    ).group_by(
        Watched.media_type
    ).with_entities(
        Watched.media_type,
        func.count(Watched.media_type)
    ).all()

    data = []
    for (name, count) in w:
        t = {"name": name, "count": count}
        data.append(t)

    return jsonify(
        success=True,
        data=data
    )
