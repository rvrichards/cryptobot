# cryptobot
Currently this will have functions that will utilize Binance and Coinbase exchanges. The Bots are coming. All code is in Python v3.

## File: binancefunctions.py
* def authenticate() - authentication to Binance. API Keys are stored as environment vars.
* def get_token_list() - Will get each token and its latest price. 
* def binance_price(number=42) - Will currnetly return EOSTUSD. Returns 42, 88, or user set # of rows.
* def clean_dates(df_dates) - leans the dates that Binance returns.
* def get_x_info(token_symbol) - Given a symbol (like EOS), get the associated assets on Binance.

## File: coinbaseFunctions.py
* def authenticate() - Authentication to Coinbase. API Keys are stored as environment vars.
* def get_token_price(token="EOS") - Retrieve the spot price of token in USD.
* def get_account_info(gettall=False) - Get token balances from account.
