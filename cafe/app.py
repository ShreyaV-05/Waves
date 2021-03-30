from flask import Blueprint

cafe_bp = Blueprint('cafe', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='assets')


@cafe_bp.route('/')
def index():
    return ""