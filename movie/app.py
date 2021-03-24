from flask import Blueprint

movie_bp = Blueprint('movie', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='assets')


@movie_bp.route('/')
def index():
    return ""