from flask import Blueprint
from flask import Blueprint, render_template, request
from flask import Flask, render_template, redirect, url_for, request

movie_bp = Blueprint('movie', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@movie_bp.route('/')
def index():
    return render_template("base.html")


@movie_bp.route('/movies', methods=["GET", "POST"])
def movies():
    if request.form:
        return render_template("movie/base.html")
