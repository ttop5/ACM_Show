# -*- coding: utf-8 -*-

from . import admin
from .mixin import ModelViewMixin
from app.models import TrainModel


class RegionalAdmin(ModelViewMixin):
    column_list = [
        'id', 'train', 'time', 'place', 'description']
    column_filters = ['train', 'place']
    column_searchable_list = ['train', 'place']

admin.add_view(
    RegionalAdmin(
        TrainModel, category=u'竞赛管理', name=u'区域赛', url='regional'
    )
)
