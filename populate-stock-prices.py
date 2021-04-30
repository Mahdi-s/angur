import sqlite3
import csv
import pandas as pd
#works --


#create database
connection = sqlite3.connect('stocks.db')
#create cursor instance
cursor = connection.cursor()


company_list_stock_prices = ['aapl-stock-prices.csv', 'amzn-stock-prices.csv', 'bby-stock-prices.csv', 'fb-stock-prices.csv', 'tsla-stock-prices.csv', 'googl-stock-prices.csv', 'ba-stock-prices.csv', 'twtr-stock-prices.csv', 'pltr-stock-prices.csv', 'wmt-stock-prices.csv']
stock_price_table_list = ['market_historical_data_apple', 'market_historical_data_amazon', 'market_historical_data_bestbuy', 'market_historical_data_facebook', 'market_historical_data_tesla', 'market_historical_data_alphabet', 'market_historical_data_boeing', 'market_historical_data_twitter', 'market_historical_data_palantir', 'market_historical_data_walmart']
index = 0
for company in company_list_stock_prices:
    file_loc = 'data/'+str(company)
    data_file = open(file_loc)
    rows = csv.reader(data_file)
    next(rows)
    query = "INSERT INTO {0} VALUES (?,?,?,?,?,?,?)".format(stock_price_table_list[index])
    cursor.executemany(query , rows)
    index +=1
    connection.commit()
