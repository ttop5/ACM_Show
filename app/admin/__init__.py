# -*- coding: utf-8 -*-

from flask import redirect, url_for, request, views
from flask.ext.login import current_user
from flask.ext.admin import Admin, AdminIndexView as _AdminIndexView
from flask.ext.admin.base import expose, expose_plugview


class AdminIndexView(_AdminIndexView):

    def is_accessible(self):
        return current_user.is_authenticated() and current_user.is_administrator()

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next=request.url))

    @expose()
    def index(self):
        return self.render('admin/index.html')

    @expose_plugview('/step/')
    class Step(views.MethodView):

        def get(self, cls):
            return cls.render('admin/index.html')

admin = Admin(
    name='ACM_SHOW 后台管理',
    index_view=AdminIndexView(name='Index'),
    template_mode='bootstrap3'
)

from .user import *
from .team import *
