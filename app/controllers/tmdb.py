import os
import requests
from flask import Blueprint, Response, jsonify, request

tmdb_bp = Blueprint('tmdb', __name__, url_prefix='/tmdb')


@tmdb_bp.get('/api/<path:url>')
def api_proxy(url):
    base_url = os.getenv("TMDB_V3_API")

    query = request.query_string.decode(
        "utf8") + "&api_key=" + os.getenv("TMDB_V3_API_KEY") + "&language=zh-CN"
    url = "{}/{}?{}".format(base_url, url, query)
    method = request.method

    resp = requests.request(method, url)

    return jsonify(resp.json())


@tmdb_bp.get('/image/<path:url>')
def image_proxy(url):
    type = request.args.get('type')
    base_url = os.getenv("TMDB_IMG_URL")
    request_url = f"{base_url}/t/p/w500/{url}"

    if type == 'original':
        request_url = f"{base_url}/t/p/original/{url}"

    resp = requests.request('GET', request_url)

    return Response(resp, mimetype=resp.headers['Content-Type'])
