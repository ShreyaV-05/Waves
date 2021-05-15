from flask import Blueprint
from flask import Flask, render_template, request

movie_bp = Blueprint('movie', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')
@movie_bp.route('/')
def bookstore():
    return render_template("theatres.html")