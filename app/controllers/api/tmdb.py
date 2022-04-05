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
    base_url = os.getenv("TMDB_IMG_URL")
    resp = requests.request('GET', f"{base_url}/t/p/w500/{url}")

    # TODO 可以区别原图还是指定大小
    return Response(resp, mimetype=resp.headers['Content-Type'])
