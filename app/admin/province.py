# -*- coding: utf-8 -*-

from . import admin
from .mixin import ModelViewMixin
from app.models import MatchModel


class ProvinceAdmin(ModelViewMixin):
    column_list = [
        'id', 'match', 'team', 'time', 'description']
    column_filters = ['match']
    column_searchable_list = ['match']


admin.add_view(
    ProvinceAdmin(
        MatchModel, category=u'竞赛管理', name=u'省赛', url='match'
    )
)
