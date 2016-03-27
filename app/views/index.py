from app import app
from flask import render_template
from app.models import RoleModel, UserModel, TeamModel, ProvinceModel, RegionalModel


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/regional')
def regional():
    regionals = RegionalModel.objects.all()
    return render_template("regional.html", regionals=regionals)


@app.route('/province')
def province():
    provinces = ProvinceModel.objects.all()
    return render_template("province.html", provinces=provinces)


@app.route('/team')
def team():
    teams = TeamModel.objects.all()
    return render_template("team.html", teams=teams)


@app.route('/coach')
def coach():
    role = RoleModel.objects(name='coach').first()
    users = UserModel.objects(roles=role).all()
    return render_template("coach.html", users=users)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")
