import yfinance as yf
import pandas as pd
import numpy as np
# import seaborn as sb
# import matplotlib.pyplot as plt


#sample information

# current information
msft = yf.Ticker("MSFT")
print (msft.info)

# price history
hist = msft.history(period="max")
print (hist)

# dividends
div = msft.dividends
print (div)

print (msft.earnings)
print (msft.cashflow)
print (msft.balance_sheet)
print (msft.recommendations)
print (msft.recommendations['To Grade'].value_counts())

import yfinance as yf


ticker = "TSLA"

msft = yf.Ticker(ticker)
stock_info = yf.Ticker(ticker).info

# get stock info
ticker_yahoo = yf.Ticker(ticker)
data = ticker_yahoo.history()
last_quote = (data.tail(1)['Close'].iloc[0])

# market_price = stock_info['regularMarketPrice']
# previous_close_price = stock_info['regularMarketPreviousClose']
# print('market price ', market_price)
# print('previous close price ', previous_close_price)

print('Date:',str(data.tail(1)['Close'].index.values[0]))
print(ticker,last_quote)

yahoo_financials = YahooFinancials('AAPL')
data = yahoo_financials.get_historical_price_data(start_date='2019-01-01', 
                                                  end_date='2019-12-31', 
                                                  time_interval='weekly')
aapl_df = pd.DataFrame(data['AAPL']['prices'])
aapl_df = aapl_df.drop('date', axis=1).set_index('formatted_date')
aapl_df.head()
import yfinance as yf

data = yf.download("AAPL", start="2022-05-01", end="2022-05-03",  interval = "1m")
tickerTag = yf.Ticker(url)
    tickerTag.actions.to_csv("tickertag{}.csv".format(url))
    f = yf.Ticker("IBM").history(start="2017-01-01", end="2017-04-30", frequency='1dy')['Close']
    data = goog.history(interval='1m', start='2022-01-03', end='2022-01-10')
data.head()
df_new['Metascore'] = df_new['Metascore'].fillna((df_new['Metascore'].mean()))