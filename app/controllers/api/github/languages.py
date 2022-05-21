import os
import json
import requests
from flask import Blueprint
from flask import jsonify

github_languages_bp = Blueprint(
    'github_languages_bp', __name__, url_prefix='/languages')

url = "https://api.github.com/graphql"


@github_languages_bp.get("")
def languages_stats():
    headers = {
        'Authorization': f"Bearer {os.getenv('GITHUB_TOKEN')}",
        'Content-Type': 'application/json'
    }

    payload = {
        "query": """
        query userInfo($login: String!) {\n
          user(login: $login) {\n
            # fetch only owner repos & not forks\n
            repositories(ownerAffiliations: OWNER, isFork: false, first: 100) {\n
              nodes {\n
                name\n
                languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {\n
                  edges {\n
                    size\n
                    node {\n
                      color\n
                      name\n
                    }\n
                  }\n
                }\n
              }\n
            }\n
          }\n
        }
      """,
        "variables": {
            "login": "seif-wu"
        }
    }

    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))

    return response.text
