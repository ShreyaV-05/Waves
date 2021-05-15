from flask import Blueprint
from flask import Flask, render_template

cafe_bp = Blueprint('cafe', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='assets')


@cafe_bp.route('/')
def cafe():
    return render_template("cafe.html")