import requests


class SimpleGroceryStoreAPI:

    def get_cart(self):
        response = requests.get('https://simple-grocery-store-api.glitch.me/cart')
        if response.status_code == 200:
            return response.json()
        else:
            return None


class TestSimpleGroceryStoreAPI:

    def test_get_cart(self):
        api = SimpleGroceryStoreAPI()
        cart = api.get_cart()
        assert cart is not None, 'Failed to get cart from API'
        assert 'items' in cart, 'Cart does not have items'
        assert isinstance(cart['items'], list), 'Cart items are not a list'


# Example usage
test_api = TestSimpleGroceryStoreAPI()
test_api.test_get_cart()
