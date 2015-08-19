# -*- coding: utf-8 -*-

from . import admin
from .mixin import ModelViewMixin
from app.models import TrainModel


class TrainAdmin(ModelViewMixin):
    column_list = [
        'id', 'train', 'time', 'place', 'description']
    column_filters = ['train', 'place']
    column_searchable_list = ['train', 'place']

admin.add_view(
    TrainAdmin(
        TrainModel, name='Train', category='Train Manage', url='train'
    )
)