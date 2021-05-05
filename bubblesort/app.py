from flask import Blueprint, render_template, request

#from bubblesort.bubblesort import Cubed
from bubblesort.bubblesort import bubbleintsort

bubblesort_bp = Blueprint('bubblesort', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')


@bubblesort_bp.route('/bubsort', methods=["GET", "POST"])
def bubblesort():
    if request.form:
        all_list = []
        b = 1 # to ensure first number is 0
        numberToItterate = 5
        # iterating through all of the form text fields input
        for i in range(numberToItterate):
            string_used = 'user_input' + str(b)
            user_input = request.form.get(string_used)
            print(user_input)
            all_list.append(int(user_input))
            b = b + 1

        print(all_list)

        return render_template("bubsort.html" , output_list = bubbleintsort(all_list))
    return render_template("bubsort.html")