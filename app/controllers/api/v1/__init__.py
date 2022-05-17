from flask import Blueprint

from .login import login_bp
from .weapp import weapp_bp

v1_bp = Blueprint('v1', __name__, url_prefix='/v1')

v1_bp.register_blueprint(login_bp)
v1_bp.register_blueprint(weapp_bp)
