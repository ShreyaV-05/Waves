from flask import Blueprint
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import projects
#importing databases
from model import caferecs, caferevs,db
#importing list for caferecs
from model import cafe_recs
#importing list for caferevs
from model import cafe_revs,buzz_revs, bing_revs, ccc_revs, ccb_revs, colombe_revs, rev_revs, moto_revs, other_revs

cafe_bp = Blueprint('cafe', name,
                    template_folder='templates',
                    static_folder='static', static_url_path='assets')


@cafe_bp.route('/')
def cafe():
    return render_template("cafe.html")

@cafe_bp.route("/caferec/", methods=['GET', 'POST'])
def caferec_route():
    if request.method == 'POST':
        caferec = request.form['caferec']
        cafereclocation = request.form['cafereclocation']
        caferecdescrip = request.form['caferecdescrip']

        #adding user into the all_user database
        new_recommendation = caferecs(caferec = caferec, cafereclocation = cafereclocation, caferecdescrip = caferecdescrip)
        db.session.add(new_recommendation)
        db.session.commit()

        return render_template("caferec.html")
    return render_template("caferec.html")

@cafe_bp.route("/caferev/", methods=['GET', 'POST'])
def caferev_route():
    if request.method == 'POST':
        caferev = request.form['caferev']
        caferevdiff = request.form['caferevdiff']
        cafereclocation = request.form['cafereclocation']
        caferevreview = request.form['author']

        #  adding user into the all_user database
        new_review = caferevs(cafeerev = caferev ,caferevdiff = caferevdiff ,cafereclocation = cafereclocation, caferevreview = caferevreview)
        db.session.add(new_review)
        db.session.commit()

        return render_template("caferev.html")
    return render_template("caferev.html")