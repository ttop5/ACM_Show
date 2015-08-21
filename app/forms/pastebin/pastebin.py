# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import Required


class PastebinForm(Form):
    poster = StringField(u'Poster', [Required()])
    syntax = SelectField(
        u'Syntax', choices=[
            ('text', 'Text'),
            ('c', 'C'),
            ('cpp', 'C++'),
            ('java', 'Java'),
            ('go', 'Go'),
            ('rb', 'Ruby'),
            ('python', 'Python'),
            ('python3', 'Python 3'),
            ('csharp', 'C#'),
            ('php', 'PHP'),
            ('html', 'HTML'),
            ('css', 'CSS'),
            ('js', 'JavaScript'),
            ('sql', 'SQL'),
            ('bash', 'Bash'),
            ('basemake', 'Makefile')
        ]
    )
    content = TextAreaField(u'Content', [Required()])
    paste = SubmitField(u'Paste')