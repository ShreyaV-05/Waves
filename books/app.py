from flask import Blueprint
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import projects
books_bp = Blueprint('books', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')
books_bp = Flask(__name__)
books_bp.config['SECRET_KEY'] = 'Books'
books_bp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
books_bp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # telling program where to put the database
db = SQLAlchemy(books_bp)  # db defined here
Bootstrap(books_bp)
records = []
#og books on genre pages
class genresep(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    genre = db.Column(db.String(100))
    book = db.Column(db.String(500))
    descrip = db.Column(db.String(1000))

    # constructor that initializes the database
    def __init__(self, genre, book, descrip):
        self.genre = genre
        self.book = book
        self.descrip = descrip
#rec books
class recs(db.Model):
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



"Create Database"
db.create_all()  # creates books.db file

@books_bp.route('/')
def index():
    return ""
"""ASK ANDREW WHAT THIS DOES AND WOULD NAVBAR BE HERE OR IN GEN HOME PAGE HMTL??"""

@books_bp.route("/rec/", methods=['GET', 'POST'])
def recs_route():
    if request.method == 'POST':
        genre= request.form['genre']
        genrediff= request.form['genrediff']
        book = request.form['book']
        author = request.form['author']
        descrip = request.form['descrip']


        #  adding user into the rec database
        new_rec = genre(genre=genre, genrediff=genrediff, book=book, author=author, descrip=descrip)
        db.session.add(new_rec)
        db.session.commit()

        return render_template("rec.html", projects=projects.setup())

    return render_template("rec.html", projects=projects.setup())
recs_recs = []
rom_recs = []
action_recs = []
fantasy_recs = []
biblio_recs = []

def recs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = recs.query.all()
    for rec in database:
        recs_dict = {'id':rec.id, 'genre': rec.genre, 'book': rec.book, 'descrip':rec.descrip}
        recs_recs.append(recs_dict)

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


genresep_pg = []
rom_pg = []
action_pg = []
fantasy_pg = []
biblio_pg = []


def genresep_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = genresep.query.all()
    for genre in database:
        genresep_dict = {'id':genresep.id, 'genre': genresep.genre, 'book': genresep.book, 'descrip':genresep.descrip}
        genresep_pg.append(genresep_dict)

        #getting the value that corresponds with the key 'location'
        genre = genresep_dict['genre']

        #if it is rom
        if genre == 'Romance':
            #append to rom books
            rom_pg.append(genresep_dict)
        #if it is action
        if genre == 'Action':
            #append to action books
            action_pg.append(genresep_dict)
        #if it is fantasy
        if genre == 'Fantasy':
            #append to fantasy books
            fantasy_pg.append(genresep_dict)
        #if it is biblio
        if genre == 'Bibliography':
            #append to bibliography books
            biblio_pg.append(genresep_dict)


@books_bp.route("/romance/")
def genretemp_route():
    return render_template("romance.html", projects=projects.setup(), genresep_table=rom_pg, recs_table=rom_recs)
@books_bp.route("/action/")
def genretemp_route_1():
    return render_template("action.html", projects=projects.setup(), genresep_table=action_pg, recs_table=action_recs)
@books_bp.route("/fantasy/")
def genretemp_route_2():
    return render_template("fantasy.html", projects=projects.setup(), genresep_table=fantasy_pg, recs_table=fantasy_recs)
@books_bp.route("/biblio/")
def genretemp_route_3():
    return render_template("biblio.html", projects=projects.setup(), genresep_table=biblio_pg, recs_table=biblio_recs)
