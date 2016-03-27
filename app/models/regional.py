# -*- coding: utf-8 -*-

from app import db
from datetime import datetime


class RegionalModel(db.Document):
    id = db.SequenceField(primary_key=True)
    name = db.StringField(required=True, max_length=255)
    time = db.DateTimeField(default=datetime.now)
    place = db.StringField(max_length=255)
    description = db.StringField()

    def __unicode__(self):
        return self.name

    meta = {
            'collection': 'regionals'
    }
