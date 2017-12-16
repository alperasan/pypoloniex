from pypoloniex import LoadPairs, TimeSeries

# # Load realtime data from Poloniex
# sess = LoadPairs()
#
# # Returns coin object
# LTC = sess.getPair(market = 'BTC', coin = 'LTC')
#
# # Quickview
# print(LTC)

# Create TimeSeries object
sess = TimeSeries()

# Parameters
pair = ('BTC', 'LTC')	 # (market, coin)
# period = 86400           # candle stick period in seconds
period = 300            # candle stick period in seconds
start = '10/1/2017'		  # dd/mm/year
end =  '11/12/2017'       # dd/mm/year

# Get time series data from Poloniex and load into pandas dataframe
sess.getData(pair, period, start, end)

# Show dataframe with parameters
sess.show()
