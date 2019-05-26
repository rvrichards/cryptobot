import datetime
import plotly.offline as py
import plotly.graph_objs as go
import pandas_datareader as web

# Get the stock market price, default to Google.

def market_price(stock='GOOGL'):
	start = datetime.datetime(2019,1,1)
	end = datetime.datetime(2019,5,1)

	STOCK = web.DataReader(stock, 'yahoo', start, end)
	# STOCK = web.DataReader(stock, 'google', start, end)   # deprecated

	data = go.Ohlc(
	    x=STOCK.index[:],
	    open=STOCK['Open'],
	    high=STOCK['High'],
	    low=STOCK['Low'],
	    close=STOCK['Close'],
	    name=stock,
	    increasing=dict(line=dict(color='blue')),
	    decreasing=dict(line=dict(color='red')),
	)

	layout = {
	    'title': stock,
	    'xaxis': {'title': 'Year to Date 2019'},
	    'yaxis': {'title': 'Price per stock ($)'}
	}
	data = dict(data=[data], layout=layout)
	return data


# Testing
print ("Starting...press cntl-c to terminate...")
data = market_price()
py.plot(data, filename='stockmarket.html')
