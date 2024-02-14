import unittest
import json
from your_flask_app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_valid_checkout_without_special_offer(self):
        # Valid token without applying special offer
        token = "valid_token"
        order = {"Crusty Chicken": 1, "New Yorker": 2}
        response = self.app.post('/checkout', headers={'Authorization': f'Bearer {token}'}, json=order)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total_price'], 19.97)

    def test_valid_checkout_with_special_offer(self):
        # Valid token with applying special offer
        token = "valid_token"
        order = {"Crusty Chicken": 2, "New Yorker": 2}
        response = self.app.post('/checkout', headers={'Authorization': f'Bearer {token}'}, json=order)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total_price'], 19.96)

    def test_invalid_token(self):
        # Invalid token
        token = "invalid_token"
        order = {"Crusty Chicken": 1, "New Yorker": 2}
        response = self.app.post('/checkout', headers={'Authorization': f'Bearer {token}'}, json=order)
        self.assertEqual(response.status_code, 401)

    def test_no_order_data(self):
        # No order data provided
        token = "valid_token"
        response = self.app.post('/checkout', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['error'], 'No order data provided')

if __name__ == '__main__':
    unittest.main()
