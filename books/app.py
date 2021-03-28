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
class genre(db.Model):
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
    book = db.Column(db.String(500))
    author = db.Column(db.String(1000))

    # constructor that initializes the database
    def __init__(self, genre, book, author):
        self.genre = genre
        self.book = book
        self.author = author



"Create Database"
db.create_all()  # creates books.db file

@books_bp.route('/')
def index():
    return ""
"""ASK ANDREW WHAT THIS DOES AND WOULD NAVBAR BE HERE OR IN GEN HOME PAGE HMTL??"""
genre_pg = []
rom_pg = []
action_pg = []
fantasy_pg = []
biblio_pg = []

def genre_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = genre.query.all()
    for genre in database:
        genre_dict = {'id':genre.id, 'cuisine': genre.genre, 'review': genre.book, 'location':genre.description}
        genre_pg.append(genre_dict)

        #getting the value that corresponds with the key 'location'
        genre = genre_dict['genre']

        #if it is rom
        if genre == 'Romance':
            #append to rom books
            rom_pg.append(genre_dict)
        #if it is action
        if genre == 'Action':
            #append to action books
            action_pg.append(genre_dict)
        #if it is fantasy
        if genre == 'Fantasy':
            #append to fantasy books
            fantasy_pg.append(genre_dict)
        #if it is biblio
        if genre == 'Bibliography':
            #append to bibliography books
            biblio_pg.append(genre_dict)


@books_bp.route("/romance/")
def genretemp_route():
    return render_template("action.html", projects=projects.setup(), genre_table=rom_pg)
@books_bp.route("/action/")
def genretemp_route_1():
    return render_template("action.html", projects=projects.setup(), genre_table=action_pg)
@books_bp.route("/fantasy/")
def genretemp_route_2():
    return render_template("fantasy.html", projects=projects.setup(), genre_table=fantasy_pg)
@books_bp.route("/biblio/")
def genretemp_route_3():
    return render_template("biblio.html", projects=projects.setup(), genre_table=biblio_pg)

@books_bp.route("/rec/", methods=['GET', 'POST'])
def recs_route():
    if request.method == 'POST':
        genre= request.form['genre']
        book = request.form['book']
        author = request.form['author']


        #  adding user into the rec database
        new_rec = genre(genre = genre,book = book, author = author)
        db.session.add(new_rec)
        db.session.commit()

        return render_template("rec.html", projects=projects.setup())

    return render_template("rec.html", projects=projects.setup())