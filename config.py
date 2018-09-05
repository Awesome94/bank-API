"""
This file contains configuration settings for the Bank APP API.

Secrets are read from environment settings.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

ENV = os.environ.get("ENV")

class BAseConfig(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
