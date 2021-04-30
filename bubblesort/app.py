from flask import Blueprint, render_template, request

#from bubblesort.bubblesort import Cubed

bubblesort_bp = Blueprint('bubblesort', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')


@bubblesort_bp.route('/bubsort', methods=["GET", "POST"])
def bubblesort():
    if request.form:
        return render_template("bubsort.html", cubed=Cubed(int(request.form.get("series"))))
    return render_template("bubsort", cubed=Cubed(2))