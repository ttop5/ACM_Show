# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    import sys
    reload(sys)  # noqa
    sys.setdefaultencoding('utf-8')

    SECRET_KEY = (
        os.environ.get('SECRET_KEY') or
        u'\x97\xfa%\xab\xd2\xc2\xf8\xfc\xef\xaeTKDk\xc0\xe1//($\xc7\xc0'
    )

    # mongodb
    MONGODB_SETTINGS = {
        'db': 'acm_show',
        'username': '',
        'password': '',
        'host': '127.0.0.1',
        'port': 27017
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
