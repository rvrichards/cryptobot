# cryptobot
Currently this will have functions that will utilize Binance exchange. The Bots are coming.
Binance specific methods.

## File: binancefunctions.py
* def authenticate() - authentication to Binance. API Keys are stored as environment vars.
* def get_token_list() - Will get each token and its latest price. 
* def binance_price(number=42) - Will currnetly return EOSTUSD. Returns 42, 88, or user set # of rows.
* def clean_dates(df_dates) - leans the dates that Binance returns.
* def get_x_info(token_symbol) - Given a symbol (like EOS), get the associated assets on Binance.