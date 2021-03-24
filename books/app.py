from flask import Blueprint

books_bp = Blueprint('books', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@books_bp.route('/')
def index():
    return ""