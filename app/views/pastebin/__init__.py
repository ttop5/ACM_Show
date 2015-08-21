from .pastebin import PastebinView
from flask import Blueprint

bp_pastebin = Blueprint('pastebin', __name__)

bp_pastebin.add_url_rule(
    '/',
    endpoint='pastebin',
    view_func=PastebinView.as_view('login'),
    methods = ['get', 'post']
)