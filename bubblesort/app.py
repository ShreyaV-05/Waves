from flask import Blueprint, render_template, request

from minilabs_diane.minilab_fib import Cubed

minilabs_diane_bp = Blueprint('minilabs_diane', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')


@minilabs_diane_bp.route('/fib', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("fib.html", cubed=Cubed(int(request.form.get("series"))))
    return render_template("fib.html", cubed=Cubed(2))