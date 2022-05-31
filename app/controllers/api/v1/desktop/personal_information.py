from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from app.utils.redis import Redis
from app.models.personal_information import PersonalInformation
from app.schema.personal_information_schema import PersonalInformationSchema

personal_information_bp = Blueprint(
    'personal_information', __name__, url_prefix='/personal_information')


@personal_information_bp.get('')
def show():
    token = request.headers.get('X-Token')
    if not token:
        return jsonify(
            success=False,
            message="令牌好像不见了",
        ), 400

    redis_key = "personal_information:{token}".format(token=token)
    data = Redis.hgetall(redis_key)
    if data:
        return data

    myself = PersonalInformation.myself()
    args = request.args
    mobile = args.get("mobile")

    if myself is None:
        return jsonify(
            success=False,
            message="糟糕，信息不存在了",
        ), 400

    if mobile != myself.mobile:
        return jsonify(
            success=False,
            message="您好像不知道联系方式",
        ), 400

    myself_schema = PersonalInformationSchema()
    result = myself_schema.dump(myself)
    Redis.hmset(redis_key, result)
    Redis.expire(redis_key, expire=86400)

    return jsonify(
        success=True,
        data=result
    )


@personal_information_bp.put('')
@jwt_required()
def update():
    myself = PersonalInformation.myself()
    if not myself:
        myself = PersonalInformation

    name = request.json.get("name", None)
    mobile = request.json.get("mobile", None)
    if not name:
        return jsonify(success=False, message="名字不能为空"), 400
    if not mobile:
        return jsonify(success=False, message="联系方式不能为空"), 400

    myself.name = name
    myself.mobile = mobile

    age = request.json.get("age", None)
    if age is not None:
        myself.age = age

    email = request.json.get("email", None)
    if email is not None:
         myself.email = email

    num_projects = request.json.get("num_projects", None)
    if num_projects is not None:
         myself.num_projects = num_projects

    work_experience = request.json.get("work_experience", None)
    if work_experience is not None:
         myself.work_experience = work_experience

    educational_background = request.json.get("educational_background", None)
    if educational_background is not None:
         myself.educational_background = educational_background

    desc = request.json.get("desc", None)
    if desc is not None:
         myself.desc = desc

    db.session.add(myself)
    db.session.commit()

    myself_schema = PersonalInformationSchema()
    result = myself_schema.dump(myself)

    return jsonify(success=True, data=result)
