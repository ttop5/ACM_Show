from app import app
from flask.ext.script import Manager, Server, Shell


manager = Manager(app)


def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(
        use_debugger=True,
        use_reloader=True,
        host="0.0.0.0",
        port=5000
    )
)

if __name__ == '__main__':
    manager.run()