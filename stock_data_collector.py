import pandas_datareader as web
company_list = ['aapl', 'amzn', 'bby', 'fb', 'tsla', 'googl', 'ba', 'twtr', 'pltr', 'wmt']
for item in company_list:
    df = web.DataReader(item, data_source='yahoo',start='2019-01-1', end='2021-04-27')
    name = str(item)+'-stock-prices.csv'
    df.to_csv(name)
