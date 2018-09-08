from flask_testing import TestCase
import json

from tests import BaseTestMixin

class TestLoadsAllEndpoints(BaseTestMixin):
    """
    Checks that all end points respond with 200 status_code when called.
    """
    def test_does_not_loads_all_users_without_token(self):
        response = self.client.get("/v1/users/")
        self.assertEqual(response.status_code, 403)

    def test_requires_token_to_get_specific_user(self):
        response = self.client.get("/v1/users/1")
        self.assertEqual(response.status_code, 403)

    def fails_to_registers_user_without_password(self):
        data=dict(firstname="awesl")
        res = self.client.post('/v1/register', data=json.dumps(data), content_type='application/json')
        result = res.json
        self.assertEqual(result['message'], "Password must be non-empty.")
        self.assertEqual(res.status_code, 401)

    def test_withdraws_from_specific_account(self):
        response = self.client.post("/v1/account/1/withdraw")
        self.assertEqual(response.status_code, 404)

    def test_deposits_on_specific_account(self):
        data=dict(account_number="112000000212", user_id=1, amount=2000 )
        response = self.client.post("/v1/account/deposit/1", data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_loads_balance_from_specific_account(self):
        response = self.client.get("/v1/account/1/balance")
        self.assertEqual(response.status_code, 200)
