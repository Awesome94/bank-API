import unittest
import os
import json
from flask_testing import TestCase
from tests import BaseTestMixin

class BankApiTestCase(BaseTestMixin, TestCase):
    """Represents the Bank API test case"""

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

    def check_balance(self):
        pass

    def test_user_logout(self):
        pass

    def test_delete_user(self):
        pass

    def test_add_bank_tellor(self):
        pass
        
    def test_create_new_account(self):
        pass

if __name__ == "__main__":
    unittest.main()
