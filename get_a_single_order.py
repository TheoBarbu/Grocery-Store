import requests

class GroceryStore:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_order(self, order_id):
        url = f"{self.base_url}/orders/{order_id}"
        response = requests.get(url)
        order = response.json()
        return order

store = GroceryStore("https://simple-grocery-store-api.glitch.me")

order_id = 1
order = store.get_order(order_id)
print(order)

def test_get_order():
    store = GroceryStore("https://simple-grocery-store-api.glitch.me")
    order_id = 1
    order = store.get_order(order_id)
    assert isinstance(order, dict)
    assert order["id"] == order_id
test_get_order()
