# -*- coding: utf-8 -*-

from .mixin import ModelViewMixin
from . import admin
from app.models import UserModel


class UserAdmin(ModelViewMixin):

    pass


admin.add_view(
    UserAdmin(
        UserModel, name='User', category='User Manager', url='user'
    )
)
