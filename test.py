import sqlite3
import csv

#create database
connection = sqlite3.connect('stocks.db')
#create cursor instance
cursor = connection.cursor()



cursor.execute("SELECT * FROM annual_income_statement_boeing")
print(cursor.fetchall())
#connection.commit()
