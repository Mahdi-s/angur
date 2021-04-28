import sqlite3
import csv

#create database
connection = sqlite3.connect('stocks.db')
#create cursor instance
c = connection.cursor()



c.execute("SELECT * FROM market_historical_data_apple")
#c.execute("SELECT * FROM annual_income_statement_apple")

print(c.fetchone())
connection.commit()
