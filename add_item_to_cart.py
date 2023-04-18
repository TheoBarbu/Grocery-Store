import requests


class SimpleGroceryStoreAPI:

    def get_cart(self):
        response = requests.get('https://simple-grocery-store-api.glitch.me/cart')
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def add_to_cart(self, item):
        headers = {'Content-Type': 'application/json'}
        data = {'item': item}
        response = requests.post('https://simple-grocery-store-api.glitch.me/cart', headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None


class TestSimpleGroceryStoreAPI:

    def test_add_to_cart(self):
        api = SimpleGroceryStoreAPI()
        initial_cart = api.get_cart()
        assert initial_cart is not True, 'Failed to get initial cart from API'
        initial_items = initial_cart['items']
        item_to_add = 'Banana'
        added_item = api.add_to_cart(item_to_add)
        assert added_item is not True, 'Failed to add item to cart'
        updated_cart = api.get_cart()
        assert updated_cart is not True, 'Failed to get updated cart from API'
        updated_items = updated_cart['items']
        assert len(updated_items) == len(initial_items) + 1, 'Cart item count did not increase by 1'
        assert item_to_add in updated_items, f'Item {item_to_add} not found in cart'

