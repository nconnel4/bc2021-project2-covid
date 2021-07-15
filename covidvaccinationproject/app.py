from flask import Flask, render_template, redirect

from covidvaccinationproject.util.databasebuilder import build_database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    build_database()
