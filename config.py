"""
This file contains configuration settings for the Bank APP API.

Secrets are read from environment settings.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

ENV = os.environ.get("ENV")

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

class StagingConfig(Config):
    DEBUG = True
    TESTING = True

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

class TestingConfig(Config):
    DEBUG = False
    TESTING = True
