from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from app import db
from .role import RoleModel
from mongoengine import DENY, NULLIFY  # noqa


class UserModel(db.Document, UserMixin):
    id = db.SequenceField(primary_key=True)
    username = db.StringField(max_length=255)
    name = db.StringField(max_length=255)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(max_length=255)
    roles = db.ListField(
        db.ReferenceField(
            RoleModel,
            reverse_delete_rule=DENY
        ),
        default=[]
    )
    grade = db.StringField(max_length=255)

    @staticmethod
    def generate_password(password):
        return generate_password_hash(password)

    def set_password(self, password):
        self.password = self.generate_password(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def create_user(cls, username, email, password, **kwargs):
        password = cls.generate_password(password)
        return cls.objects.create(
            username=username,
            email=email,
            password=password,
            **kwargs
        )
