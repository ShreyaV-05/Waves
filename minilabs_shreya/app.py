from flask import Blueprint, render_template, request
from minilabs_shreya.prime_numbers import PrimeNum

minilabs_shreya_bp = Blueprint('minilabs_shreya_bp', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')


@minilabs_shreya_bp.route('/prime_numbers', methods=["GET", "POST"])
def prime():
    if request.form:
        return render_template("prime_numbers.html", primenum=PrimeNum(int(request.form.get("series"))))
    return render_template("prime_numbers.html", primenum=PrimeNum(2))
