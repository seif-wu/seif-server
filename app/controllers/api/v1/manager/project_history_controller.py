from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app import db
from app.models.project_history import ProjectHistory
from app.schema.project_history_schema import ProjectHistorySchema

project_history_bp = Blueprint(
    'project_history', __name__, url_prefix='/project_history')


@project_history_bp.post('')
@jwt_required()
def create():
    w = ProjectHistory(
        project_name=request.json.get("project_name", None),
        time_period=request.json.get("time_period", None),
        jobs=request.json.get("jobs", None),
        desc=request.json.get("desc", None),
        personal_information_id=request.json.get(
            "personal_information_id", None),
    )

    db.session.add(w)
    db.session.commit()

    w_schema = ProjectHistorySchema()
    result = w_schema.dump(w)

    return jsonify(success=True, data=result)
