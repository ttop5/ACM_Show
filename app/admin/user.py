# -*- coding: utf-8 -*-

from wtforms import fields

from .mixin import ModelViewMixin
from . import admin
from app.models import UserModel, RoleModel


class UserAdmin(ModelViewMixin):
    column_list = [
        'id', 'username', 'roles', 'nickname', 'email', 'grade', 'created_at']
    column_filters = ['username', 'nickname', 'email', 'grade']
    column_searchable_list = ['username', 'nickname', 'email', 'grade']


    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.password2 = fields.StringField('Password')
        return form_class

    def on_model_change(self, form, model):
        if len(model.password2):
            model.password = UserModel.generate_password(form.password2.data)
        elif not model.password:
            model.password = UserModel.generate_password('12345678')


class RoleAdmin(ModelViewMixin):
    column_list = [
        'name', 'description', 'created_at']
    column_filters = ['name']
    column_searchable_list = ['name']

    form_excluded_columns = ['created_at']


admin.add_view(
    UserAdmin(
        UserModel, name='User', category='User Manage', url='user'
    )
)
admin.add_view(
    RoleAdmin(
        RoleModel, name='Role', category='User Manage', url='role'
    )
)
