from flask import Blueprint

mini_labs_bp = Blueprint('mini_labs', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')


@mini_labs_bp.route('/')
def index():
    return ""