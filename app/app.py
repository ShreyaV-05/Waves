import main

from flask import Flask, render_template
#blueprints for books
from books.app import books_bp
#blueprints for groc
from groc.app import groc_bp
#blueprints for cafe
from cafe.app import cafe_bp

app = Flask(__name__)
app.register_blueprint(books_bp, url_prefix='/books/')
app.register_blueprint(groc_bp, url_prefix='/groc/')
app.register_blueprint(cafe_bp, url_prefix='/cafe/')




#create a Flask instance
app = Flask(__name__)


@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')

