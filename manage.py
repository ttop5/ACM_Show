from app import app
from flask.ext.script import Manager, Server, Shell
from app.models import UserModel, RoleModel

manager = Manager(app)


def make_shell_context():
    return dict(app=app, UserModel=UserModel, RoleModel=RoleModel)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(
        use_debugger=True,
        use_reloader=True,
        host="0.0.0.0",
        port=5000
    )
)


@manager.command
def deploy():
    RoleModel.insert_roles()
    admin = RoleModel.objects(name='admin').first()

    user = UserModel.objects(username='admin').first()
    if user is None:
        user = UserModel.create_user(
            username='admin',
            email='ttop5@qq.com',
            password='123'
        )
        user.roles.append(admin)
        user.save()

if __name__ == '__main__':
    manager.run()
