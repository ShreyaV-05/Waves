from flask import Blueprint, render_template, request
from minilabs_andrea.myfibonacci import Exponential

minilabs_andrea_bp = Blueprint('minilabs_andrea', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')


@minlabs_andrea_bp.route('/', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("myfibonacci.html", fibonacci=Exponential(int(request.form.get("series"))))
    return render_template("myfibonacci.html", fibonacci=Exponential(2))
