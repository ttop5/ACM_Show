from .pastebin import PastebinView, ShareView
from flask import Blueprint

bp_pastebin = Blueprint('pastebin', __name__)

bp_pastebin.add_url_rule(
    '/',
    endpoint='pastebin',
    view_func=PastebinView.as_view('pastebin'),
    methods = ['get', 'post']
)

bp_pastebin.add_url_rule(
    '/<int:id>',
    endpoint='share',
    view_func=ShareView.as_view('share'),
    methods = ['get']
)