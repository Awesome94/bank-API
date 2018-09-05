"""
This file contains configuration settings for the Bank APP API.

Secrets are read from environment settings.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

ENV = os.environ.get("ENV")

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    pass
class StagingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
class DevelopmentConfig(BaseConfig):
    DEBUG = False
    TESTING = True
class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
