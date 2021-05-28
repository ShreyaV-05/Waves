from flask import Blueprint
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import projects
books_bp = Blueprint('books', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')
@books_bp.route('/')
def store():
    return render_template("store.html")




"""
--------------------------------------------------------------------------------------------------------------------
#rec books
class bookrecs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    genre = db.Column(db.String(100))
    genrediff = db.Column(db.String(100))
    book = db.Column(db.String(500))
    author = db.Column(db.String(500))
    descrip = db.Column(db.String(1000))

    # constructor that initializes the database
    def __init__(self, genre,genrediff, book, author,descrip):
        self.genre = genre
        self.genrediff = genrediff
        self.book = book
        self.author = author
        self.descrip = descrip
--------------------------------------------------------------------------------------------------------------------
#rev books
class bookrevs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    genre = db.Column(db.String(100))
    genrediff = db.Column(db.String(100))
    book = db.Column(db.String(1000))
    author = db.Column(db.String(500))
    review = db.Column(db.String(1000))

    # constructor that initializes the database
    def __init__(self, genre,genrediff, book, author,review):
        self.genre = genre
        self.genrediff = genrediff
        self.book = book
        self.author = author
        self.review = review
--------------------------------------------------------------------------------------------------------------------
#rec store
class storerecs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    storerec = db.Column(db.String(1000))
    reclocation = db.Column(db.String(1000))
    recdescrip = db.Column(db.String(1000))


    # constructor that initializes the database
    def __init__(self, storerec,reclocation, recdescrip):
        self.storerec = storerec
        self.reclocation = reclocation
        self.recdescrip = recdescrip
--------------------------------------------------------------------------------------------------------------------
#rev store
class storerevs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    storerev = db.Column(db.String(1000))
    storerevdiff = db.Column(db.String(1000))
    revlocation = db.Column(db.String(1000))
    revreview = db.Column(db.String(1000))


    # constructor that initializes the database
    def __init__(self, storerev,storerevdiff, revlocation, recreview):
        self.storerev = storerev
        self.storerevdiff = storerevdiff
        self.revlocation = revlocation
        self.revreview = revreview


--------------------------------------------------------------------------------------------------------------------
"Create Database"
db.create_all()  # creates books.db file
--------------------------------------------------------------------------------------------------------------------
@book_bp.route("/bookrec/", methods=['GET', 'POST'])
def bookrec_route():
    if request.method == 'POST':
       genre = request.form['genre']
       genrediff = request.form['genrediff']
       book = request.form['book']
       author = request.form['author']
       descrip = request.form['descrip']


        #  adding user into the all_user database
        new_recommendation = (genre = genre ,genrediff = genrediff ,book = book,author = author, descrip = descrip)
        db.session.add(new_recommendation)
        db.session.commit()

        return render_template("bookrec.html", projects=projects.setup())

    return render_template("bookrec.html", projects=projects.setup())
books_recs = []
action_recs = []
fantasy_recs = []
rom_recs = []
biblio_recs = []
other_recs = []
def bookrecs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = bookrecs.query.all()
    for rec in database:
        recs_dict = {'id':rec.id, 'genre': rec.genre, 'book': rec.book, 'descrip':rec.descrip}
        books_recs.append(recs_dict)

        #getting the value that corresponds with the key 'location'
        genre = recs_dict['genre']

        #if it is rom
        if genre == 'Romance':
            #append to rom books
            rom_recs.append(recs_dict)
        #if it is action
        if genre == 'Action':
            #append to action books
            action_recs.append(recs_dict)
        #if it is fantasy
        if genre == 'Fantasy':
            #append to fantasy books
            fantasy_recs.append(recs_dict)
        #if it is biblio
        if genre == 'Bibliography':
            #append to bibliography books
            biblio_recs.append(recs_dict)
        #if it is other
        if genre == 'Other':
            #append to other books
            other_recs.append(recs_dict)
--------------------------------------------------------------------------------------------------------------------
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

    return render_template("bookrev.html", projects=projects.setup())
books_revs = []
action_revs = []
fantasy_revs = []
rom_revs = []
biblio_revs = []
other_revs = []
def bookrevs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = bookrevs.query.all()
    for rev in database:
        revs_dict = {'id':rev.id, 'genre': rev.genre, 'book': rev.book, 'review':rev.review}
        books_revs.append(revs_dict)

        #getting the value that corresponds with the key 'genre'
        genre = revs_dict['genre']

        #if it is rom
        if genre == 'Romance':
            #append to rom books
            rom_revs.append(revs_dict)
        #if it is action
        if genre == 'Action':
            #append to action books
            action_revs.append(revs_dict)
        #if it is fantasy
        if genre == 'Fantasy':
            #append to fantasy books
            fantasy_revs.append(revs_dict)
        #if it is biblio
        if genre == 'Bibliography':
            #append to bibliography books
            biblio_revs.append(revs_dict)
        #if it is other
        if genre == 'Other':
            #append to other books
            other_revs.append(revs_dict)
--------------------------------------------------------------------------------------------------------------------
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

    return render_template("storerec.html", projects=projects.setup())


def storerecs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = storerecs.query.all()
    for rec in database:
        recs_dict = {'id':rec.id,'store': rec.storerec,'location': rec.reclocation, 'descrip':rec.recdescrip }
        store_recs.append(recs_dict)
--------------------------------------------------------------------------------------------------------------------        
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

    return render_template("storerev.html", projects=projects.setup())
store_revs = []
art_revs = []
faren_revs = []
ban_revs = []
beach_revs = []
verb_revs = []
other_revs = []
def storerevs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = storerevs.query.all()
    for rev in database:
        revs_dict = {'id':rev.id,'store': rev.storerev,'different': rev.storerevdiff, 'location':rev.revlocation, 'review':rev.revreview }
        store_revs.append(revs_dict)
        
        #getting the value that corresponds with the key 'store'
        store = revs_dict['store']

        #if it is Artifact
        if store == 'Artifact':
            #append to Artifact store
            art_revs.append(revs_dict)
        #if it is Farenheit
        if store == 'Farenheit':
            #append to Farenheit store
            faren_revs.append(revs_dict)
        #if it is ban
        if store == 'BAN':
            #append to ban store
            ban_revs.append(revs_dict)
        #if it is beach
        if store == 'Beach':
            #append to beach store
            beach_revs.append(revs_dict)
        #if it is verb
        if store == 'Verbatim':
            #append to verb store
            verb_revs.append(revs_dict)
        #if it is other
        if store == 'Other':
            #append to other store
            other_revs.append(revs_dict)
"""