from flask import ( # noqa
    render_template
)
from flask.views import MethodView


class PastebinView(MethodView):

    def get(self):
        return render_template('pastebin/pastebin.html')

    def post(self):
        pass