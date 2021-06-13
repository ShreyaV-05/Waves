from app import app
import os
from flask_sqlalchemy import SQLAlchemy
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

#rec cafe
class caferecs(db.Model):
    tablename = 'caferecs'
    id = db.Column(db.Integer(), primary_key=True)
    caferec = db.Column(db.String(1000))
    cafereclocation =  db.Column(db.String(1000))
    caferecdescrip = db.Column(db.String(1000))


    # constructor that initializes the database
    def init(self, caferec,cafereclocation, caferecdescrip):
        self.caferec = caferec
        self.cafereclocation = cafereclocation
        self.caferecdescrip = caferecdescrip

#rev cafe
class caferevs(db.Model):
    tablename = 'caferevs'
    id = db.Column(db.Integer(), primary_key=True)
    caferev = db.Column(db.String(1000))
    caferevdiff = db.Column(db.String(1000))
    caferevlocation = db.Column(db.String(1000))
    caferevreview = db.Column(db.String(1000))


    # constructor that initializes the database
    def init(self, caferev,caferevdiff, caferevlocation, caferevreview):
        self.caferev = caferev
        self.caferevdiff = caferevdiff
        self.caferevlocation = caferevlocation
        self.caferevreview = caferevreview

#andrea
#rev theaters
class movierevs(db.Model):
    tablename = 'movierevs'
    id = db.Column(db.Integer(), primary_key=True)
    movierev = db.Column(db.String(1000))
    movierevdiff = db.Column(db.String(1000))
    movierevlocation = db.Column(db.String(1000))
    movierevreview = db.Column(db.String(1000))


    # constructor that initializes the database
    def init(self, movierev,movierevdiff, movierevlocation, movierevreview):
        self.movierev = movierev
        self.movierevdiff = movierevdiff
        self.movierevlocation = movierevlocation
        self.movierevreview = movierevreview

db.create_all()

review_list = []

def review_map():
    review = RatingGeneral.query.all()
    for user in review:
        review_info = {'id': user.id, 'store': user.store, 'name': user.name, 'user': user.user, 'stars': user.stars, 'description': user.description}
        review_list.append(review_info)
review_map()
# print(review_list)
books_recs = []
action_recs = []
fantasy_recs = []
rom_recs = []
other_recs = []
def bookrecs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = bookrecs.query.all()
    for rec in database:
        recs_dict = {'id':rec.id, 'genre': rec.genre, 'book': rec.book, 'descrip':rec.descrip, 'author': rec.author}
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
other_revs = []
def bookrevs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = bookrevs.query.all()
    for rev in database:
        revs_dict = {'id':rev.id, 'genre': rev.genre, 'book': rev.book, 'review':rev.review, 'genrediff': rev.genrediff, 'author': rev.author}
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

cafe_recs = []
def caferecs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = caferecs.query.all()
    for rec in database:
        recs_dict = {'id':rec.id,'cafe': rec.caferec,'location': rec.cafereclocation, 'descrip':rec.caferecdescrip }
        cafe_recs.append(recs_dict)
caferecs_map()
print(cafe_recs)



cafe_revs = []
buzz_revs = []
bing_revs = []
ccc_revs = []
ccb_revs = []
colombe_revs = []
rev_revs = []
moto_revs = []
other_revs = []
def caferevs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = caferevs.query.all()
    for rev in database:
        revs_dict = {'id':rev.id,'cafe': rev.caferev,'different': rev.caferevdiff, 'location':rev.caferevlocation, 'review':rev.caferevreview }
        cafe_revs.append(revs_dict)

        #getting the value that corresponds with the key 'store'
        cafe = revs_dict['cafe']

        #if it is buzz
        if cafe == 'Buzz':
            #append to buzz store
            buzz_revs.append(revs_dict)
        #if it is bing
        if cafe == 'Bing':
            #append to bing store
            bing_revs.append(revs_dict)
        #if it is ccc
        if cafe == 'CCC':
            #append to ccc store
            ccc_revs.append(revs_dict)
        #if it is CCB
        if cafe == 'CCB':
            #append to CCB store
            ccb_revs.append(revs_dict)
        #if it is Colombe
        if cafe == 'Colombe':
            #append to Colombe store
            colombe_revs.append(revs_dict)
            #if it is Revolution
        if cafe == 'Revolution':
            #append to Revolution store
            rev_revs.append(revs_dict)
            #if it is Moto
        if cafe == 'Moto':
            #append to Moto store
            moto_revs.append(revs_dict)
        #if it is other
        if cafe == 'Other':
            #append to other store
            other_revs.append(revs_dict)
caferevs_map()
print(cafe_revs)

edwards_revs = []
angelika_revs = []
cinepolis_revs = []
movie_revs = []
other_revs = []
def movierevs_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste
    database = movierevs.query.all()
    for rev in database:
        revs_dict = {'id':rev.id,'movie': rev.caferev,'different': rev.movierevdiff, 'location':rev.movierevlocation, 'review':rev.movierevreview}
        movie_revs.append(revs_dict)

        #getting the value that corresponds with the key 'store'
        theater = revs_dict['movie']

        #if it is edwards
        if theater == 'edwards':
            #append to edwards
            edwards_revs.append(revs_dict)
        #if it is angelika
        if theater == 'angelika':
            #append to angelika
            angelika_revs.append(revs_dict)
        #if it is cinepolis
        if theater == 'cinepolis':
            #append to cinepolis
            cinepolis_revs.append(revs_dict)
        #if it is other
        if theater == 'other':
            #append to other store
            other_revs.append(revs_dict)

