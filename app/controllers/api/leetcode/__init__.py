from flask import Blueprint

from .question_progress import leetcode_question_progress_bp

leetcode_bp = Blueprint('leetcode', __name__, url_prefix='/leetcode')
leetcode_bp.register_blueprint(leetcode_question_progress_bp)
