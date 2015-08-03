from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ac_life')
def ac_life():
    return render_template("ac_life.html")


@app.route('/ac_team')
def ac_team():
    return render_template("ac_team.html")


@app.route('/ac_coach')
def ac_coach():
    return render_template("ac_coach.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")
