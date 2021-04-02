from flask import Blueprint

minilabs_andrea_bp = Blueprint('mini_labs', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')


@minilabs_andrea_bp.route('/')
def index():
    return ""