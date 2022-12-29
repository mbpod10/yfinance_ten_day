# import yfinance as yf

# ticker = yf.Ticker('GOOGL').info
# market_price = ticker['regularMarketPrice']
# previous_close_price = ticker['regularMarketPreviousClose']
# print('Ticker: GOOGL')
# print('Market Price:', market_price)
# print('Previous Close Price:', previous_close_price)
# import yfinance as yf
from datetime import datetime

# Set the start and end date
start_date = '2022-12-18'
end_date = '2022-12-29'

# Set the ticker
ticker = 'GOOGL'

# Get the data
# data = yf.download(ticker, start_date, end_date)

# Print the last 5 rows
# print(data['Close'])
print(datetime.now())
