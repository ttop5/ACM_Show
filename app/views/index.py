from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/acm_train')
def ac_train():
    return render_template("acm_train.html")


@app.route('/acm_match')
def ac_match():
    return render_template("acm_match.html")


@app.route('/acm_team')
def ac_team():
    return render_template("acm_team.html")


@app.route('/acm_coach')
def ac_coach():
    return render_template("acm_coach.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")


@app.route('/admin/index')
def admin_index():
    return render_template("admin/index.html")
