from app import app, db
from flask_testing import TestCase
import os

TEST_DB = 'test.db'

class BaseTestMixin(TestCase):
    def create_app(self):
        """
        Configure and return the Flask app
        """
        app.config.from_object('config.TestingConfig')
        return app

    def setUp(self):
        """
        Define test variables and initialize app.
        Set up a blank database for each test.
        """
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Destroy blank bank database after each test"""
        db.drop_all()
