import requests
import json
import time

# Print out price of EOS every 10 seconds
while True :
    response = requests.get("https://api.coinbase.com/v2/prices/EOS-USD/spot")
    data = response.json()
    token = data["data"]["base"]
    price = data["data"]["amount"]
    print (f"Price: {token} {price}")
    time.sleep(10)