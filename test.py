import unittest
import json
from app import app


class TestPromoUsage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_checkout_with_promo(self):
        order_data = {
            "Crusty Chicken": 2,
            "New Yorker": 1
        }
        response = self.app.post(
            '/checkout', headers={"Authorization": "Bearer <YOUR_TOKEN>"}, json=order_data)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(data["total_price"], 12.97, places=2)

    def test_checkout_without_promo(self):
        order_data = {
            "Crusty Chicken": 2,
            "New Yorker": 1
        }
        response = self.app.post(
            '/checkout', headers={"Authorization": "Bearer <YOUR_TOKEN>"}, json=order_data)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(data["total_price"], 17.97, places=2)

    def test_invalid_token(self):
        order_data = {
            "Crusty Chicken": 2,
            "New Yorker": 1
        }
        response = self.app.post(
            '/checkout', headers={"Authorization": "Bearer invalid_token"}, json=order_data)
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["error"], "Invalid token, please log in again")


if __name__ == '__main__':
    unittest.main()
