import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

from bubblesort.app import bubblesort_bp


#blueprints for books
from books.app import books_bp
#blueprints for groc
from groc.app import groc_bp
#blueprints for cafe
from cafe.app import cafe_bp
#blueprints for movie
from movie.app import movie_bp

#blueprints for minilab
from minilabs_andrea.app import minilabs_andrea_bp
from minilabs_shreya.app import minilabs_shreya_bp
from minilabs_diane.app import minilabs_diane_bp
from minilabs_ryan.app import minilabs_ryan_bp
from bubblesort.app import bubblesort_bp


app = Flask(__name__)
#Creating database
app.config['SECRET_KEY'] = 'mysecret'
basedir = os.path.abspath(os.path.dirname(__file__))
#Adding database in current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Creating a database table
class RatingGeneral(db.Model):
    __tablename__ = 'RatingGeneral'

    id = db.Column(db.Integer, primary_key=True)
    store = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    user = db.Column(db.String(100))
    time = db.Column(db.DateTime, nullable = True)
    stars = db.Column(db.Float(10))
    description = db.Column(db.String(1000))
#rec books
class bookrecs(db.Model):
    __tablename__ = 'Bookrecs'
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

#rev books
class bookrevs(db.Model):
    __tablename__ = 'Bookrevs'
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
#rec store
class storerecs(db.Model):
    __tablename__ = 'Storerecs'
    id = db.Column(db.Integer(), primary_key=True)
    storerec = db.Column(db.String(1000))
    reclocation = db.Column(db.String(1000))
    recdescrip = db.Column(db.String(1000))


    # constructor that initializes the database
    def __init__(self, storerec,reclocation, recdescrip):
        self.storerec = storerec
        self.reclocation = reclocation
        self.recdescrip = recdescrip
#rev store
class storerevs(db.Model):
    __tablename__ = 'Storerevs'
    id = db.Column(db.Integer(), primary_key=True)
    storerev = db.Column(db.String(1000))
    storerevdiff = db.Column(db.String(1000))
    revlocation = db.Column(db.String(1000))
    revreview = db.Column(db.String(1000))


    # constructor that initializes the database
    def __init__(self, storerev,storerevdiff, revlocation, revreview):
        self.storerev = storerev
        self.storerevdiff = storerevdiff
        self.revlocation = revlocation
        self.revreview = revreview

db.create_all()

review_list = []

def review_map():
    review = RatingGeneral.query.all()
    for user in review:
        review_info = {'id': user.id, 'store': user.store, 'name': user.name, 'user': user.user, 'stars': user.stars, 'description': user.description}
        review_list.append(review_info)


review_map()
# print(review_list)

app.register_blueprint(groc_bp, url_prefix='/groc')
app.register_blueprint(cafe_bp, url_prefix='/cafe')
app.register_blueprint(movie_bp, url_prefix='/movie')
app.register_blueprint(books_bp, url_prefix='/books')

app.register_blueprint(minilabs_shreya_bp, url_prefix='/minilabs_shreya')
app.register_blueprint(minilabs_andrea_bp, url_prefix='/minilabs_andrea')
app.register_blueprint(minilabs_diane_bp, url_prefix='/minilabs_diane')
app.register_blueprint(minilabs_ryan_bp, url_prefix='/ryan')
app.register_blueprint(bubblesort_bp, url_prefix='/bubblesort')






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

bookrecs_map()
# print out the contents of book recs
print(books_recs)
print("rom_rec:"+str(rom_recs))

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
bookrevs_map()
print(books_revs)

store_recs = []
def storerecs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = storerecs.query.all()
    for rec in database:
        recs_dict = {'id':rec.id,'store': rec.storerec,'location': rec.reclocation, 'descrip':rec.recdescrip }
        store_recs.append(recs_dict)
storerecs_map()
print(store_recs)

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
storerevs_map()
print(store_revs)

@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")


@app.route("/SEARCHBAR")
def SEARCHBAR_route():
    return render_template("SEARCHBAR.html")

@app.route("/review")
def review_route():
    return render_template("review.html", review=review_list)

if __name__ == "__main__":
    #runs the application on the repl development server/raspberry pi
    app.run(debug=True, port='8080', host='127.0.0.1')
