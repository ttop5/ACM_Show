from app import app
from flask import render_template
from app.models import RoleModel, UserModel, TeamModel, MatchModel, TrainModel


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/regional')
def ac_train():
    trains = TrainModel.objects.all()
    return render_template("regional.html", trains=trains)


@app.route('/province')
def ac_match():
    matches = MatchModel.objects.all()
    return render_template("province.html", matches=matches)


@app.route('/team')
def ac_team():
    teams = TeamModel.objects.all()
    return render_template("team.html", teams=teams)


@app.route('/coach')
def ac_coach():
    role = RoleModel.objects(name='coach').first()
    users = UserModel.objects(roles=role).all()
    return render_template("coach.html", users=users)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")
