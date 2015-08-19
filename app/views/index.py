from app import app
from flask import render_template
from app.models import RoleModel, UserModel, TeamModel, MatchModel, TrainModel


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/acm_train')
def ac_train():
    trains = TrainModel.objects.all()
    return render_template("ouracm/acm_train.html", trains=trains)


@app.route('/acm_match')
def ac_match():
    matches = MatchModel.objects.all()
    return render_template("ouracm/acm_match.html", matches=matches)


@app.route('/acm_team')
def ac_team():
    teams = TeamModel.objects.all()
    return render_template("ouracm/acm_team.html", teams=teams)


@app.route('/acm_coach')
def ac_coach():
    role = RoleModel.objects(name='coach').first()
    users = UserModel.objects(roles=role).all()
    return render_template("ouracm/acm_coach.html", users=users)


@app.route('/statistical_charts')
def statistical_charts():
    return render_template("statistical_charts/statistical_charts.php")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")
