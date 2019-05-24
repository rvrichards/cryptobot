import os
from binance.client import Client
from datetime import datetime
from pandas import DataFrame as df

def get_token_list():
    # Will get each token and its latest price. 
    # Returns a DataFrame 
    client = Client(api_key=os.environ.get('BINANCE_KEY'), api_secret=os.environ.get('BINANCE_SECRET'))
    tokens = client.get_all_tickers()
    tokens_df = df(tokens)
    return tokens_df


def binance_price():
    # Get some EOS data - comes back as a list of lists. This is raw looking data.
    # The docs show we have date/time, open, high, low, close price, volume, ...
    # This will get a list of 42 items.
    client = Client(api_key=os.environ.get('BINANCE_KEY'), api_secret=os.environ.get('BINANCE_SECRET'))
    candles = client.get_klines(symbol='EOSTUSD', interval=Client.KLINE_INTERVAL_1HOUR, limit=42) 

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


def clean_dates(df_dates):
    dates = []

    # Convert the date data "number" to a date we can work with. Remove milliseconds by division.
    # In this case the uncleaned data looks like: "1558562400000"
    for time in df_dates:
        fixed = datetime.fromtimestamp(int(time/1000))
        dates.append(fixed)

    # Let's convert it to a DataFrame and change the column name.
    df_fixed_date = df(dates)
    df_fixed_date.columns = ['date']    
    return df_fixed_date  




# Test the methods.......
# print (binance_price())  
# print(get_token_list())
