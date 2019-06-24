import os
from coinbase.wallet.client import Client
import requests
import json
from pprint import pprint

# Authenticate to Coinbase.
def authenticate():
    print ("in authenticate...")
    return Client(os.environ.get('COINBASE_KEY'), os.environ.get('COINBASE_SECRET'))


# Retrieve the spot price of token in USD
# Doesn't need authentication
def get_token_price(token="EOS"):
    response = requests.get("https://api.coinbase.com/v2/prices/"+token+"-USD/spot")
    data = response.json()
    token = data["data"]["base"]
    price = data["data"]["amount"]
    return (f"Price: {token} {price} USD")
   

# Get buy, sell, and spot prices  
# Use authenticate so we don't need to call 3 endpoints 
def get_token_prices(token="EOS"):
	d = dict();
	client=authenticate()
	d['token']= token
	d['buy']  = client.get_buy_price(currency_pair = 'EOS-USD')['amount']
	d['sell'] = client.get_sell_price(currency_pair = 'EOS-USD')['amount']
	d['spot'] = client.get_spot_price(currency_pair = 'EOS-USD')['amount']
	return d


def get_currencies():
	# No need for auth, use endpoints.
	response = requests.get("https://api.coinbase.com/v2/currencies")
	return response.json()


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
# print (get_token_price("XR"))
# pprint (get_currencies())

print (get_token_prices())


# pa=client.get_primary_account()
# print ("\nPrimary Account:", pa)

# user = client.get_current_user()
# print ("\nCurrent user:", user)
# print ("\nCurrent user json: ", json.dumps(user))
# account.get_transactions()
