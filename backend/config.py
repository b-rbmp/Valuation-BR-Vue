# -*- coding: utf-8 -*-
"""Flask configuration."""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """Base config."""
    FLASK_APP = 'wsgi.py'
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True