from flask import Blueprint
from flask import Flask, render_template, request

groc_bp = Blueprint('groc', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='assets')


@groc_bp.route('/')
def bookstore():
    return render_template("groc.html")