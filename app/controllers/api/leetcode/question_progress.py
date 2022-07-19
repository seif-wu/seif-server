import json
import requests
from flask import Blueprint

from app import cache

leetcode_question_progress_bp = Blueprint(
    'leetcode_question_progress_bp', __name__, url_prefix='/question_progress')

url = "https://leetcode.cn/graphql/"


@leetcode_question_progress_bp.get("")
@cache.cached(timeout=300)
def question_progress():
    # TODO 名称写活
    payload = json.dumps({
        "query": "\n    query userQuestionProgress($userSlug: String!) {\n  userProfileUserQuestionProgress(userSlug: $userSlug) {\n    numAcceptedQuestions {\n      difficulty\n      count\n    }\n    numFailedQuestions {\n      difficulty\n      count\n    }\n    numUntouchedQuestions {\n      difficulty\n      count\n    }\n  }\n}\n    ",
        "variables": {
            "userSlug": "xifo"
        }
    })

    headers = {
      'authority': 'leetcode.cn',
      'accept': '*/*',
      'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
      'content-type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

