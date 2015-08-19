# -*- coding: utf-8 -*-

from app import db
from .user import UserModel
from datetime import datetime
from mongoengine import DENY, NULLIFY  # noqa


class TeamModel(db.Document):
    id = db.SequenceField(primary_key=True)
    name = db.StringField(required=True, max_length=255)
    mem1 = db.ReferenceField(
        UserModel,
        reverse_delete_rule=DENY,
    )
    mem2 = db.ReferenceField(
        UserModel,
        reverse_delete_rule=DENY,
    )
    mem3 = db.ReferenceField(
        UserModel,
        reverse_delete_rule=DENY,
    )
    grade = db.StringField(max_length=255)
    description = db.StringField()
    created_at = db.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.name

    meta = {
            'collection': 'teams'
    }