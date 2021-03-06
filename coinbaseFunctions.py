import os
from coinbase.wallet.client import Client
import requests
import json
from pprint import pprint

# Coinbase
# account_id - is the account (wallet) to a specific token.
#            - The EOS account is: efacbfc0-eaeb-5675-a72d-a8fcc597fe2e
# user_id - is the user id of the user at coinbase. User many different accounts associated.
#         - The User id is: aa1a4bc6-2d4e-5665-aeef-ee1a23418884


# Authenticate to Coinbase.
def authenticate():
    print ("in authenticate...")
    return Client(os.environ.get('COINBASE_KEY'), os.environ.get('COINBASE_SECRET'))


def get_user_id(client):
	return client.get_current_user()['id']


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


def get_account_id(token="EOS"):
	client = authenticate()
	accounts = client.get_accounts()
	for wallet in accounts.data:
		if wallet['currency'] == token:
			return wallet['id'] 
	return


def get_account_ids(gettall=False):
	total = 0
	ball = []
	client = authenticate()
	accounts = client.get_accounts()
	for wallet in accounts.data:
		if gettall:
			ball.append(wallet['name'] + " - " + wallet['id'])
		elif float(wallet['balance']['amount']) > 0.0:
			ball.append(wallet['name'] + " - " + wallet['id'])
	return ball


def get_account_balances(gettall=False):
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


# Test uses
print ("Let's roll...")
# client=authenticate()
# pprint (get_account_ids(True))
# pprint (get_account_balances())
# print (get_token_price())
# print (get_token_price("XR"))
# pprint (get_currencies())
# print (get_token_prices())

# pa=client.get_primary_account()     # A call using https://github.com/coinbase/coinbase-python
# print ("\nPrimary Account:", pa)

# user = client.get_current_user()
# print ("\nCurrent user:", user)
# print ("\nCurrent user json: ", json.dumps(user))
# account.get_transactions()

# print (get_user_id(authenticate()))

# print (get_account_id("EOS"))
