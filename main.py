
from flask import Flask, render_template

from bubblesort.app import bubblesort_bp

"""
#blueprints for books
from books.app import books_bp
#blueprints for groc
from groc.app import groc_bp
#blueprints for cafe
from cafe.app import cafe_bp
#blueprints for movie
from movie.app import movie_bp
"""
#blueprints for minilab
from minilabs_andrea.app import minilabs_andrea_bp
from minilabs_shreya.app import minilabs_shreya_bp
from minilabs_diane.app import minilabs_diane_bp
from minilabs_ryan.app import minilabs_ryan_bp
from bubblesort.app import bubblesort_bp


app = Flask(__name__)
"""
app.register_blueprint(groc_bp, url_prefix='/groc')
app.register_blueprint(cafe_bp, url_prefix='/cafe')
app.register_blueprint(movie_bp, url_prefix='/movie')
app.register_blueprint(books_bp, url_prefix='/books')
"""
app.register_blueprint(minilabs_shreya_bp, url_prefix='/minilabs_shreya')
app.register_blueprint(minilabs_andrea_bp, url_prefix='/minilabs_andrea')
app.register_blueprint(minilabs_diane_bp, url_prefix='/minilabs_diane')
app.register_blueprint(minilabs_ryan_bp, url_prefix='/ryan')
app.register_blueprint(bubblesort_bp, url_prefix='/bubblesort')



@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

if __name__ == "__main__":
    #runs the application on the repl development server/raspberry pi
    app.run(debug=True, port='8080', host='192.168.0.24')
    """
import main

from flask import Flask, render_template
#blueprints for books
from books.app import books_bp
#blueprints for groc
from groc.app import groc_bp
#blueprints for cafe
from cafe.app import cafe_bp
#blueprints for movie
from movie.app import movie_bp
#blueprints for minilab
#from minilabs_andrea.app import waves_fibbonacci_bp

app = Flask(__name__)
app.register_blueprint(groc_bp, url_prefix='/groc')
app.register_blueprint(cafe_bp, url_prefix='/cafe')
app.register_blueprint(movie_bp, url_prefix='/movie')
app.register_blueprint(books_bp, url_prefix='/books')
#app.register_blueprint(waves_fibbonacci_bp, url_prefix='/andrea')

#create a Flask instance


@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

if __name__ == "__main__":
    #runs the application on the repl development server/raspberry pi
    app.run(debug=True, port='8080', host='127.0.0.1')

"""