from flask import Blueprint

from .user import github_user_bp

github_bp = Blueprint('github', __name__, url_prefix='/github')
github_bp.register_blueprint(github_user_bp)
