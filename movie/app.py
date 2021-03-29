from flask import Blueprint
from flask import Blueprint, render_template, request

movie_bp = Blueprint('movie', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='assets')


@movie_bp.route('/')
def index():
    return ""







@movie_bp.route('/movies', methods=["GET", "POST"])
def movies():
    if request.form:
        return render_template("movie/base.html")
