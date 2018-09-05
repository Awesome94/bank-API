import unittest
import os
import json
from app import create_app, db

class BankApiTestCase(unittest.TestCase):
    """Represents the Bank API test case"""

    def setUp(self):
        """
        Define test variables and initialize app.
        Set up a blank database for each test.
        """
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Destroy blank bank database after each test"""
        db.drop_all()

    def test_user_registration(self):
        pass
    def test_user_login(self):
        pass
    def test_account_number_generated(self):
        pass
    def test_deposit(self):
        pass
    def test_withdraw(self):
        pass
    def test_user_logout(self):
        pass

if __name__ == "__main__":
    unittest.main()
