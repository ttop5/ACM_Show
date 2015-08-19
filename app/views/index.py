from app import app
from flask import render_template
from app.models import RoleModel, UserModel, TeamModel


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
    teams = TeamModel.objects.all()
    return render_template("acm_team.html", teams=teams)


@app.route('/acm_coach')
def ac_coach():
    role = RoleModel.objects(name='coach').first()
    users = UserModel.objects(roles=role).all()
    return render_template("acm_coach.html", users=users)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")
