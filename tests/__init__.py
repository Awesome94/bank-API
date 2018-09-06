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
        self.user_data = {
            "firstname":"awesome1",
        	"email": "m2@gmeal.com",
        	"lastname":"david",
        	"password_hash":"meandme",
        	"user_type":"bank_teller",
        	"id_type":"passport",
        	"id_number":"b1416932",
        	"phone_number":"093101313"
        }
        db.create_all()

    def tearDown(self):
        """Destroy blank bank database after each test"""
        basedir = os.path.abspath(os.path.dirname(__file__))
        db.drop_all()
        os.remove(os.path.join(basedir, TEST_DB))
