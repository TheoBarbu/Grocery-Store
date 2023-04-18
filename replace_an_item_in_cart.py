import requests
import json

url = "https://simple-grocery-store-api.glitch.me/cart"

item = {
    "name": "Apples",
    "quantity": 2,
    "price": 1.50
}

new_item = {
    "name": "Bananas",
    "quantity": 4,
    "price": 0.50
}

class TestCart:
    def test_replace_item(self):
        response = requests.post(url, json=item)
        assert response.status_code == 200

        response = requests.put(url, json=new_item)
        assert response.status_code == 200

        response = requests.get(url)
        assert response.status_code == 200
        cart = response.json()
        assert len(cart) == 1
        assert cart[0]["name"] == "Bananas"
        assert cart[0]["quantity"] == 4
        assert cart[0]["price"] == 0.50

test = TestCart()
test.test_replace_item()
