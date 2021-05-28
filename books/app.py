from flask import Blueprint
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import projects
#importing databases
from model import bookrecs, bookrevs, storerecs, storerevs,db
#importing list for bookrecs
from model import books_recs, action_recs, fantasy_recs, rom_recs, biblio_recs, other_recs
#importing list for bookrevs
from model import books_revs, action_revs, fantasy_revs, rom_revs, biblio_revs, other_revs
#importing list for storerecs
from model import store_recs
#importing list for storerevs
from model import store_revs, art_revs, faren_revs, ban_revs, beach_revs, verb_revs, other_revs
books_bp = Blueprint('books', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')
@books_bp.route('/store/')
def store():
    return render_template("store.html")

@books_bp.route("/bookrec/", methods=['GET', 'POST'])
def bookrec_route():
    if request.method == 'POST':
       genre = request.form['genre']
       genrediff = request.form['genrediff']
       book = request.form['book']
       author = request.form['author']
       descrip = request.form['descrip']


       #adding user into the all_user database
       new_recommendation = bookrecs(genre = genre ,genrediff = genrediff ,book = book,author = author, descrip = descrip)
       db.session.add(new_recommendation)
       db.session.commit()

       return render_template("bookrec.html")
    return render_template("bookrec.html")

@books_bp.route("/printdb/")
def printdb_route():
    return render_template("printdb.html", books_recs=books_recs )
"""
@book_bp.route("/bookrev/", methods=['GET', 'POST'])
def bookrev_route():
    if request.method == 'POST':
       genre = request.form['genre']
       genrediff = request.form['genrediff']
       book = request.form['book']
       author = request.form['author']
       review = request.form['review']


        #  adding user into the all_user database
        new_review = (genre = genre ,genrediff = genrediff ,book = book,author = author, review = review)
        db.session.add(new_review)
        db.session.commit()

        return render_template("bookrev.html", projects=projects.setup())


def storerec_route():
    if request.method == 'POST':
       storerec = request.form['storerec']
       reclocation = request.form['reclocation']
       recdescrip = request.form['recdescrip']

        #  adding user into the all_user database
        new_recommendation = (storerec = storerec, reclocation = reclocation, recdescrip = recdescrip)
        db.session.add(new_recommendation)
        db.session.commit()

        return render_template("storerec.html", projects=projects.setup())

@book_bp.route("/storerev/", methods=['GET', 'POST'])
def storerev_route():
    if request.method == 'POST':
       storerev = request.form['storerev']
       storerevdiff = request.form['storerevdiff']
       reclocation = request.form['reclocation']
       revreview = request.form['author']

        #  adding user into the all_user database
        new_review = (storerev = storerev ,storerevdiff = storerevdiff ,reclocation = reclocation, revreview = revreview)
        db.session.add(new_recommendation)
        db.session.commit()

        return render_template("storerev.html", projects=projects.setup())

"""

