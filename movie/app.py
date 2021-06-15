from flask import Blueprint
from flask import Flask, render_template, request
#importing databases
from model import movierevs,db
#importing list for movierevs
from model import edwards_revs, angelika_revs, cinepolis_revs, movie_revs, other_revs

movie_bp = Blueprint('movie', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@movie_bp.route("/")
def theatres():
    return render_template("theatres.html")

@movie_bp.route('/movierev', methods=['GET', 'POST'])
def movierev_route():
    if request.method == 'POST':
        movierev = request.form['movierev']
        movierevdiff = request.form['movierevdiff']
        moviereclocation = request.form['moviereclocation']
        movierevreview = request.form['movierevreview']

        #  adding user into the all_user database
        new_review = movierevs(movieerev = movierev ,movierevdiff = movierevdiff ,moviereclocation = moviereclocation, movierevreview = movierevreview)
        db.session.add(new_review)
        db.session.commit()

        return render_template("movierev.html")
    return render_template("movierev.html")


