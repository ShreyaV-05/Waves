from flask import Blueprint, render_template, request
from minilabs_ryan.minilab_odd import PrimeNum
minilabs_ryan_bp = Blueprint('ryan', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')



@minilabs_ryan_bp.route('/fibonacci', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("minilabs_ryan/odd.html", fibonacci=PrimeNum(int(request.form.get("series"))))
    return render_template("minilabs_ryan/odd.html", fibonacci=PrimeNum(2))