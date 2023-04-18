import requests

class GroceryStore:
    def __init__(self, base_url):
        self.base_url = base_url

    def delete_order(self, order):
        url = self.base_url + "/orders"
        headers = {"Content-Type": "application/json"}
        params = {"name": order["name"], "item": order["item"]}

        response = requests.delete(url, headers=headers, json=params)

        if response.status_code == 200:
            return True
        else:
            return False

class TestGroceryStore:
    def test_delete_order(self):
        store = GroceryStore("https://simple-grocery-store-api.glitch.me")
        order = {"name": "Alice", "item": "apple"}
        result = store.delete_order(order)
        assert result == True, f'ERROR, Expected: True, Actual:{result}'


