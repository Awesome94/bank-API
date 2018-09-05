from flask_testing import TestCase

from tests import BaseTestMixin

class TestLoadsAllEndpoints(BaseTestMixin, TestCase):
    """
    Checks that all end points respond with 200 status_code when called.
    """
    def test_loads_all_users(self):
        response = self.client.get("v1/users")
        self.assertEqual(response.status_code, 200)

    def test_gets_specific_user(self):
        response = self.client.get("v1/user/id")
        self.assertEqual(response.status_code, 200)

    def test_registers_user(self):
        response = self.client.get("v1/register")
        self.assertEqual(response.status_code, 200)

    def test_withdraws_from_specific_account(self):
        response = self.client.get("v1/account/<id>/withdraw")
        self.assertEqual(response.status_code, 200)

    def test_deposits_on_specific_account(self):
        response = self.client.get("v1/account/<id>/deposit")
        self.assertEqual(response.status_code, 200)

    def test_loads_balance_from_specific_account(self):
        response = self.client.get("v1/account/<id>/balance")
        self.assertEqual(response.status_code, 200)