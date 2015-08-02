from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ac_life')
def aclife():
    return render_template("ac_life.html")

@app.route('/ac_team')
def acteam():
    return render_template("ac_team.html")

@app.route('/ac_coach')
def accoach():
    return render_template("ac_coach.html")