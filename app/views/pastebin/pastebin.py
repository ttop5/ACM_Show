from flask import ( # noqa
    render_template
)
from flask.views import MethodView
from app.forms import PastebinForm


class PastebinView(MethodView):

    template = 'pastebin/pastebin.html'

    def get(self):
        form = PastebinForm()
        return render_template(self.template, form=form)

    def post(self):

        pass