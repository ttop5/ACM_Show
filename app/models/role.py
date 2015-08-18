# -*- coding: utf-8 -*-
from app import db
from datetime import datetime


class RoleModel(db.Document):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now, required=True)

    @staticmethod
    def insert_roles():
        roles = {
            'admin': '管理员',
            'coach': '教练',
            'member': '队员'
        }
        for r in roles:
            role = RoleModel.objects(name=r).first()
            if role is None:
                role =  RoleModel(name=r)
            role.description = roles[r]
            role.save()

    def __unicode__(self):
        return self.name

    meta = {
        'collection': 'Role'
    }