from flask import Blueprint

from .personal_information import personal_information_bp

desktop_bp = Blueprint('desktop', __name__, url_prefix='/desktop')
desktop_bp.register_blueprint(personal_information_bp)
