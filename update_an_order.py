import requests

class SimpleGroceryStoreAPI:
    def __init__(self, url):
        self.url = url

    def update_order(self, order):
        response = requests.put(self.url + "/orders", json=order)
        return response.json()

documentation = SimpleGroceryStoreAPI("https://simple-grocery-store-api.glitch.me")

order = {
    "customer_name": "Ioana Luna",
    "customer_email": "ioana.luna@example.com",
    "items": [
        {
            "name": "Apples",
            "quantity": 3,
            "price": 0.50
        },
        {
            "name": "Bananas",
            "quantity": 2,
            "price": 0.25
        }
    ],
    "total": 2.00
}

updated_order = documentation.update_order(order)
print(updated_order)

def test_update_order():
    documentation = SimpleGroceryStoreAPI("https://simple-grocery-store-api.glitch.me")

    order = {
        "customer_name": "Ioana Luna",
        "customer_email": "ioana.luna@example.com",
        "items": [
            {
                "name": "Apples",
                "quantity": 3,
                "price": 0.50
            },
            {
                "name": "Bananas",
                "quantity": 2,
                "price": 0.25
            }
        ],
        "total": 2.00
    }

    updated_order = documentation.update_order(order)

    assert updated_order["customer_name"] == "Ioana Luna"
    assert updated_order["customer_email"] == "ioana.luna@example.com"
    assert updated_order["items"][0]["name"] == "Apples"
    assert updated_order["items"][0]["quantity"] == 3
    assert updated_order["items"][0]["price"] == 0.50
    assert updated_order["items"][1]["name"] == "Bananas"
    assert updated_order["items"][1]["quantity"] == 2
    assert updated_order["items"][1]["price"] == 0.25
    assert updated_order["total"] == 2.00

    order["customer_name"] = "Iulia Luna"
    updated_order = documentation.update_order(order)

    # Check if the updated order has the new data
    assert updated_order["customer_name"] == "Iulia Luna"
