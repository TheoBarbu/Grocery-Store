import requests

API_ENDPOINT = 'https://simple-grocery-store-api.glitch.me/orders'

class TestNewOrder:
    def test_create_new_order(self):
        payload = {
            'customer_name': 'John Doe',
            'items': [
                {'name': 'apples', 'quantity': 2},
                {'name': 'bananas', 'quantity': 3},
                {'name': 'oranges', 'quantity': 1}
            ]
        }

        response = requests.post(API_ENDPOINT, json=payload)
        assert response.status_code == 201
        expected_keys = ['id', 'customer_name', 'items', 'total_price']
        assert all(key in response.json() for key in expected_keys)
        assert response.json()['customer_name'] == payload['customer_name']
        assert response.json()['items'] == payload['items']
