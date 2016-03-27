# -*- coding: utf-8 -*-

from app import db
from .team import TeamModel
from datetime import datetime
from mongoengine import DENY, NULLIFY  # noqa


class RegionalModel(db.Document):
    id = db.SequenceField(primary_key=True)
    name = db.StringField(required=True, max_length=255)
    team = db.ReferenceField(
        TeamModel,
        reverse_delete_rule=DENY,
    )
    time = db.DateTimeField(default=datetime.now)
    place = db.StringField(max_length=255)
    description = db.StringField()

    def __unicode__(self):
        return self.name

    meta = {
            'collection': 'regionals'
    }
