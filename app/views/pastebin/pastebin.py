from flask import ( # noqa
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView
from app.forms import PastebinForm
from app.models import PastebinModel


class ShareView(MethodView):

    template = 'pastebin/share.html'

    def get(self, id):
        return render_template(self.template)



class PastebinView(MethodView):

    template = 'pastebin/pastebin.html'

    def get(self):
        form = PastebinForm()
        return render_template(self.template, form=form)

    def post(self):
        form =PastebinForm()
        p = PastebinModel.objects.create(
            poster=form.poster.data,
            syntax=form.syntax.data,
            content=form.content.data
        )
        return redirect(url_for('pastebin.share', id=p.id))