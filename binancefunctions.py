import os
import pandas as pd
from binance.client import Client
from datetime import datetime
from pandas import DataFrame as df

# Binance specific methods.
# - def authenticate():
# - def get_token_list():
# - def binance_price(number=42):
# - def clean_dates(df_dates):
# - def get_x_info(token_symbol):

# Authenticate to Binance.
def authenticate():
    print ("Authenticating...")
    return Client(api_key=os.environ.get('BINANCE_KEY'), api_secret=os.environ.get('BINANCE_SECRET'))


# Will get each token and its latest price. 
def get_token_list(): 
    client = authenticate()
    tokens = client.get_all_tickers()
    tokens_df = df(tokens)
    return tokens_df


# Get some EOS data - comes back as a list of lists. This is raw looking data.
# The docs show we have date/time, open, high, low, close price, volume, ...
# This will get a default list of 42 items, unless a non int is passed, then 88.
# Returns a DataFrame.
def binance_price(number=42):
    client = authenticate()
    if not isinstance(number, int):
        number = 88
    print ("Getting ", number, " EOSTUSD hourly prices...", sep="")
    candles = client.get_klines(symbol='EOSTUSD', interval=Client.KLINE_INTERVAL_1HOUR, limit=number) 

    # Let's make it look nicer, a dataframe! Returns 11 columns and 42 rows (500 is default/max)
    candles_df = df(candles)

    # Send the date column (col 0) to the clean_dates function to return a Python readable date format as a DataFrame.
    good_date = clean_dates(candles_df[0])

    candles_df.pop(0)     # Remove column date
    candles_df.pop(11)    # Remove column 11 (docs say to ignore this column)

    # final_df = candles_df.join(df_good_date)
    final_df = candles_df.join(good_date)
    final_df.set_index('date', inplace=True)

    final_df.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Asset Volume', 'Trades', 'Taker Base', 'Taker Quote']
    return final_df


# Cleans the dates that Binance returns.
# Binance uncleaned date data looks like: "1558562400000"
def clean_dates(df_dates):
    dates = []
 
    for time in df_dates:
        fixed = datetime.fromtimestamp(int(time/1000))   # Remove milliseconds by division.
        dates.append(fixed)

    # Let's convert it to a DataFrame and change the column name.
    df_fixed_date = df(dates)
    df_fixed_date.columns = ['date']    
    return df_fixed_date  


# Given a symbol, get the associated assets on Binance.
def get_x_info(token_symbol):
    client = authenticate()
    print ("Getting Binanaces tokens using ", token_symbol, ".", sep="")
    tokens = client.get_exchange_info()
    tokens_df= pd.DataFrame(tokens['symbols'])
    tokens_df= tokens_df[['symbol', 'baseAsset',  'quoteAsset']]
    tokens_df.set_index('symbol', inplace=True)     # "inplace" is used to remove index column of just numbers
    tokens_df= tokens_df[tokens_df['baseAsset'] == token_symbol]
    tokens_df.set_index('baseAsset')
    return tokens_df


# Test the methods.......
# print (binance_price("test"))  
# print(get_token_list())
# print ("Lets go")
# print ( get_x_info('EOS') )