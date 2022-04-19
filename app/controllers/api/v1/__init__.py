from flask import Blueprint

from .login import login_bp

v1_bp = Blueprint('login', __name__, url_prefix='/v1')

v1_bp.register_blueprint(login_bp)
