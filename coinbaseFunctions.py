import os
from coinbase.wallet.client import Client
import requests
from pprint import pprint

# Authenticate to Coinbase.
def authenticate():
    print ("in authenticate...")
    return Client(os.environ.get('COINBASE_KEY'), os.environ.get('COINBASE_SECRET'))


# Retrieve the spot price of token in USD
def get_token_price(token="EOS"):
    response = requests.get("https://api.coinbase.com/v2/prices/"+token+"-USD/spot")
    data = response.json()
    token = data["data"]["base"]
    price = data["data"]["amount"]
    return (f"Price: {token} {price} USD")
    

def get_account_info(gettall=False):
	total = 0
	ball = []
	client = authenticate()
	accounts = client.get_accounts()
	for wallet in accounts.data:
		if gettall:
			ball.append(wallet['name'] + " - " + wallet['balance']['amount'])
		elif float(wallet['balance']['amount']) > 0.0:
			ball.append(wallet['name'] + " - " + wallet['balance']['amount'])
	return ball

print ("Let's roll...")
# pprint (get_account_info(True))
# print (get_token_price())
print (get_token_price("XR"))

