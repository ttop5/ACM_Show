# -*- coding: utf-8 -*-

from . import admin
from .mixin import ModelViewMixin
from app.models import RegionalModel


class RegionalAdmin(ModelViewMixin):
    column_list = [
        'id', 'name', 'time', 'place', 'description']
    column_filters = ['name', 'place']
    column_searchable_list = ['name', 'place']

admin.add_view(
    RegionalAdmin(
        RegionalModel, category=u'竞赛管理', name=u'区域赛', url='regional'
    )
)
