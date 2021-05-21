from flask import Blueprint
from flask import Flask, render_template, request

movie_bp = Blueprint('movie', __name__,
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@movie_bp.route('/')
def bookstore():
    return render_template("theatres.html")


"""
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'  # telling program where to put the database
db = SQLAlchemy(app)  # db defined here
Bootstrap(app)
records = []

# class defines database -- what rows you want in database
class Movies(db.Model):
    email = db.Column('item_id', db.String(50), primary_key=True)
    theatre = db.Column(db.String(100))
    location = db.Column(db.String(50))
    price = db.Column(db.String(50))
    
# constructor that initializes the database
def __init__(self, email, theatre, location, price):
    self.email = email
    self.theatre = theatre
    self.location = location
    self.price = price
    
"Create Database"
db.create_all()  # creates movies.db file    



class MovieForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Length(min=1, max=80)])
    theatre = StringField('theatre', validators=[InputRequired(), Length(min=1, max=80)])
    location = StringField('location', validators=[InputRequired()])
    price = StringField('price', validators=[InputRequired()])
    
  
    
# shows what is in the database even if you reload the program (preserving the existence of the items in the database)
# showing old items in the table
def list_map():  # mapping the front end to  backend, put in the function so we don't have to copy paste all the time
    movie = Movies.query.all()
    for movie in movie:
        user_dict = {'email': movie.email, 'theatre': movie.theatre, 'location': movie.location,
                     'price': food.price}
        records.append(user_dict)
        # records is a list initiated at top of code, showcases all the items appending to the database


# calling the method list_map()
list_map()
@app.route("/recommend/", methods=['GET', "POST"])
def rec_route():
    form = MovieForm()
    if form.validate_on_submit():  # adding in all
        new_movie = Movies(email=form.email.data, theatre=form.theatre.data, location=form.location.data,
                            price=form.price.data)
        db.session.add(new_movie)
        db.session.commit()
        user_dict = {'email': new_movie.email, 'theatre': new_movie.theatre, 'location': new_movie.location,
                     'price': new_food.price}
        records.append(user_dict)  # adding a new item to the table
    return render_template("recommend.html", form=form, table=records)
@app.route('/delete/', methods=['GET', "POST"])
def delete():
    # print("arrived to delete")  # for debugging in the terminal
    if request.method == "POST":  # we know the item id
        email_id = request.form["item_id"] #retrieving the value of the email address
        for dictionary in records:  # deleteing items from the data base
            if (dictionary["email"] == email_id):
                # print("we found it")  # for debugging in the terminal
                delete = Movies.query.filter_by(email=email_id).first()
                db.session.delete(delete)
                db.session.commit()
                #print("after delete")  # for debuggin in the terminal
            for i in range(len(records)):  # deleting the front end view of the data base
                if records[i]['email'] == cuisine_id:
                    del records[i]
                    break
    else:
        print("could not find the value")
    return redirect(url_for('rec_route'))

"""
