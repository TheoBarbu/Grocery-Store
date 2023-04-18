import requests

class GroceryStore:
    def __init__(self):
        self.products = []

    def get_all_products(self):
        response = requests.get('https://simple-grocery-store-api.glitch.me/products')
        if response.status_code == 200:
            self.products = response.json()
            return True
        return False

def test_grocery_store():
    # Get all products
    store = GroceryStore()
    assert store.get_all_products() == True
    assert len(store.products) > 0


if __name__ == '__main__':
    test_grocery_store()
