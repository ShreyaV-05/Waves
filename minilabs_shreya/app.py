from flask import Blueprint, render_template, request
from minilabs_shreya.fibonacci import Fibonacci

minilabs_shreya_bp = Blueprint('shreya', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')


@minilabs_shreya_bp.route('/fibonacci', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("algorithm/fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))))
    return render_template("algorithm/fibonacci.html", fibonacci=Fibonacci(2))
