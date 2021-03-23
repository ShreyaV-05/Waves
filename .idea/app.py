import main

from flask import Flask, render_template

#create a Flask instance
app = Flask(__name__)


@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')

    delete this when u see it