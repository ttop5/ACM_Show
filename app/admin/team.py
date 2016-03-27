# -*- coding: utf-8 -*-

from . import admin
from .mixin import ModelViewMixin
from app.models import TeamModel

class TeamAdmin(ModelViewMixin):
    column_list = [
        'id', 'name', 'mem1', 'mem2', 'mem3', 'description', 'grade', 'created_at']
    column_filters = ['name', 'grade']
    column_searchable_list = ['name', 'grade']


admin.add_view(
    TeamAdmin(
        TeamModel, category=u'队伍管理', name=u'队伍管理', url='team'
    )
)
