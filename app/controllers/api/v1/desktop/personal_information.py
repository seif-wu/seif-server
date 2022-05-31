from flask import Blueprint, jsonify, request
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
        )

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
        )

    if mobile != myself.mobile:
        return jsonify(
            success=False,
            message="您好像不知道联系方式",
        )

    myself_schema = PersonalInformationSchema()
    result = myself_schema.dump(myself)
    Redis.hmset(redis_key, result)
    Redis.expire(redis_key, expire=86400)

    return jsonify(
        success=True,
        data=result
    )
