# -*- coding: utf-8 -*-

from .mixin import ModelViewMixin
from . import admin
from app.models import UserModel, RoleModel


class UserAdmin(ModelViewMixin):
    column_list = [
        'id', 'username', 'roles', 'nickname', 'email', 'grade']
    column_filters = ['username', 'nickname', 'email', 'grade']
    column_searchable_list = ['username', 'nickname', 'email', 'grade']

admin.add_view(
    UserAdmin(
        UserModel, name='User', category='User Manage', url='user'
    )
)
