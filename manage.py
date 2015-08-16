from app import app
from flask.ext.script import Manager, Server, Shell
from app.models import UserModel

manager = Manager(app)


def make_shell_context():
    return dict(app=app, UserModel=UserModel)

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
    user = UserModel.objects(username='admin').first()
    if user is None:
        user = UserModel.create_user(
            username='admin',
            email='ttop5@qq.com',
            password='123'
        ) 

if __name__ == '__main__':
    manager.run()
