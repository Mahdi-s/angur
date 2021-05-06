import sqlite3
import csv
import pandas as pd

#create database
connection = sqlite3.connect('stocks.db')
#create cursor instance
cursor = connection.cursor()



file_loc = 'data/calulated-ratios.csv'
data_file = open(file_loc)
rows = csv.reader(data_file)
next(rows)

query = "INSERT INTO calculated_ratios VALUES (?,?,?,?)"
cursor.executemany(query , rows)
connection.commit()
