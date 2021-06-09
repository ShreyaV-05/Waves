from app import app
from flask import Flask, render_template, url_for
from model import review_list
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

app.register_blueprint(groc_bp, url_prefix='/groc')
app.register_blueprint(cafe_bp, url_prefix='/cafe')
app.register_blueprint(movie_bp, url_prefix='/movie')
app.register_blueprint(books_bp, url_prefix='/books')

app.register_blueprint(minilabs_shreya_bp, url_prefix='/minilabs_shreya')
app.register_blueprint(minilabs_andrea_bp, url_prefix='/minilabs_andrea')
app.register_blueprint(minilabs_diane_bp, url_prefix='/minilabs_diane')
app.register_blueprint(minilabs_ryan_bp, url_prefix='/ryan')
app.register_blueprint(bubblesort_bp, url_prefix='/bubblesort')

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

@app.route('/restapi/quote/', methods=['GET', 'POST'])
def quote():
    # call to random quote web api
    import requests

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    querystring = {"language_code":"en"}

    headers = {
        'x-rapidapi-key': "be43b38cedmsh17c4689e2c1a95fp18da84jsnd77b7103f602",
        'x-rapidapi-host': "quotes15.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #quote = response.text

    start1 = 'ent":'
    end1 = ',"ur'
    quote1 = response.text[response.text.find(start1)+len(start1):response.text.find(end1)+len(start1)-5]

    quote = quote1

    return render_template("home.html", Title="Home", quote=quote)

if __name__ == "__main__":
    app.run(debug=True, port='8080', host='127.0.0.1')
