# -*- coding: utf-8 -*-

from . import admin
from .mixin import ModelViewMixin
from app.models import MatchModel


class MatchAdmin(ModelViewMixin):
    column_list = [
        'id', 'match', 'team', 'time', 'description']
    column_filters = ['match']
    column_searchable_list = ['match']


admin.add_view(
    MatchAdmin(
        MatchModel, name='Match', category='Match Manage', url='match'
    )
)