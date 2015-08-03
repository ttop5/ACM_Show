# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import PasswordField, StringField, BooleanField, SubmitField
from wtforms.validators import Email, Required, ValidationError

from app.models import UserModel


class LoginForm(Form):
    email = StringField(u'E-mail', [Required(), Email()])
    password = PasswordField(u'Passwd', [Required()])
    remember_me = BooleanField(u'Remember Me')
    submit = SubmitField(u'Sign in')

    def validate_password(self, field):
        user = UserModel.objects.filter(
            email=self.email.data
        ).first()
        if user is not None and user.verify_password(field.data):
            self.user = user
        else:
            raise ValidationError('Email or password is invalid')