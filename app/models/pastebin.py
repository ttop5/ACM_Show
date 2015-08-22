# -*- coding: utf-8 -*-

from app import db


class PastebinModel(db.Document):
    id = db.SequenceField(primary_key=True)
    poster = db.StringField(required=True, max_length=255)
    syntax = db.StringField(required=True, max_length=255)
    content = db.StringField(required=True)

    def __unicode__(self):
        return self.name

    meta = {
            'collection': 'pastebin'
    }