from flask import Blueprint

from .work_history_controller import work_history_bp

manager_bp = Blueprint('manager', __name__, url_prefix='/manager')
manager_bp.register_blueprint(work_history_bp)
