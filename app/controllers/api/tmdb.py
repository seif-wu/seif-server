import os
import requests
from flask import Blueprint, jsonify, request

tmdb_bp = Blueprint('tmdb', __name__, url_prefix='/tmdb')


@tmdb_bp.get('/<path:url>')
def proxy(url):
    base_url = os.getenv("TMDB_V3_API")

    query = request.query_string.decode(
        "utf8") + "&api_key=" + os.getenv("TMDB_V3_API_KEY") + "&language=zh-CN"
    url = "{}/{}?{}".format(base_url, url, query)
    method = request.method

    resp = requests.request(method, url)

    return jsonify(resp.json())
