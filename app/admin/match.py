# -*- coding: utf-8 -*-

from . import admin
from .mixin import ModelViewMixin
from app.models import MatchModel


class MatchAdmin(ModelViewMixin):
    pass

admin.add_view(
    MatchAdmin(
        MatchModel, name='Match', category='Match Manage', url='match'
    )
)