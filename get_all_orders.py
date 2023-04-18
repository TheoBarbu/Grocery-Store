import requests
class GroceryStore:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_orders(self):
        url = f"{self.base_url}/orders"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        orders = response.json()
        return orders

store = GroceryStore("https://simple-grocery-store-api.glitch.me", "your_token_here")

# get all orders
orders = store.get_orders()
print(orders)

def test_get_orders():
    store = GroceryStore("https://simple-grocery-store-api.glitch.me", "your_token_here")
    orders = store.get_orders()
    assert len(orders) > 0
    assert all("id" in order for order in orders)
test_get_orders()
