from flask import Blueprint

groc_bp = Blueprint('groc', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@groc_bp.route('/')
def index():
    return ""