# -*- coding: utf-8 -*-

from . import admin
from .mixin import ModelViewMixin
from app.models import ProvinceModel


class ProvinceAdmin(ModelViewMixin):
    column_list = [
        'id', 'name', 'team', 'time', 'description']
    column_filters = ['name']
    column_searchable_list = ['name']


admin.add_view(
    ProvinceAdmin(
        ProvinceModel, category=u'竞赛管理', name=u'省赛', url='match'
    )
)
