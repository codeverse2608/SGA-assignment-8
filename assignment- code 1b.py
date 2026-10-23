import requests

SERVER = "http://127.0.0.1:5000"

# 1. Get latest menu
response = requests.get(SERVER + "/menu")
menu = response.json()
print("Latest Menu:")
print(menu)

# 2. Place an order
order = {"item": "Poha", "quantity": 2}

response = requests.post(
    SERVER + "/order",
    json=order
)

result = response.json()
print("Order Result:")
print(result)