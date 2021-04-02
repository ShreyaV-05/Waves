from flask import Blueprint, render_template, request

from minilabs_diane.fibonacci import Fibonacci

minilabs_diane_bp = Blueprint('diane', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')


@minilabs_diane_bp.route('/fibonacci', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("minilabs_diane/fib.html", fibonacci=Fibonacci(int(request.form.get("series"))))
    return render_template("minilabs_diane/fib.html", fibonacci=Fibonacci(2))