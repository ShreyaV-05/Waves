from flask import Blueprint, render_template, request
from minilabs_ryan.minilab_odd import Odd
minilabs_ryan_bp = Blueprint('ryan', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')



@minilabs_ryan_bp.route('/odd', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("minilabs_ryan/odd.html", odd=Odd(int(request.form.get("series"))))
    return render_template("minilabs_ryan/odd.html", odd=Odd(2))