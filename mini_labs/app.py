from flask import Blueprint

labs_bp = Blueprint('groc', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='assets')


@labs_bp.route('/')
def index():
    return ""