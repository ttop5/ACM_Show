# -*- coding: utf-8 -*-

from . import admin
from .mixin import ModelViewMixin
from app.models import TrainModel


class TrainAdmin(ModelViewMixin):
    pass

admin.add_view(
    TrainAdmin(
        TrainModel, name='Train', category='Train Manage', url='train'
    )
)