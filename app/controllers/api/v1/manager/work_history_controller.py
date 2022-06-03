from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app import db
from app.models.work_history import WorkHistory
from app.schema.work_history_schema import WorkHistorySchema

work_history_bp = Blueprint(
    'work_history', __name__, url_prefix='/work_history')


@work_history_bp.post('')
@jwt_required()
def create():
    w = WorkHistory(
        company_name=request.json.get("company_name", None),
        time_period=request.json.get("time_period", None),
        jobs=request.json.get("jobs", None),
        desc=request.json.get("desc", None),
        personal_information_id=request.json.get(
            "personal_information_id", None),
    )

    db.session.add(w)
    db.session.commit()

    w_schema = WorkHistorySchema()
    result = w_schema.dump(w)

    return jsonify(success=True, data=result)
