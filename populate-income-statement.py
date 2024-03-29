import sqlite3
import csv
import pandas as pd

#create database
connection = sqlite3.connect('stocks.db')
#create cursor instance
cursor = connection.cursor()


company_list = ['apple-income-statement.csv', 'amazon-income-statement.csv', 'bestbuy-income-statement.csv', 'facebook-income-statement.csv', 'tesla-income-statement.csv', 'alphabet-income-statement.csv', 'boeing-income-statement.csv', 'twitter-income-statement.csv', 'palantir-income-statement.csv', 'walmart-income-statement.csv']
table_list = ['annual_income_statement_apple', 'annual_income_statement_amazon', 'annual_income_statement_bestbuy', 'annual_income_statement_facebook', 'annual_income_statement_tesla', 'annual_income_statement_alphabet', 'annual_income_statement_boeing', 'annual_income_statement_twitter', 'annual_income_statement_palantir', 'annual_income_statement_walmart']
index = 0
data = []

for company in company_list:
    file_loc = 'data/'+str(company)
    data_file = open(file_loc)
    rows = csv.reader(data_file)
    next(rows)

    for row in rows:
        for i, item in enumerate(row):
            row[i] = item.strip(' $,()').replace(',','')
            if item == '-':
                row[i] = ''
        data.append(row)

    #print(data)
    # print(company)
    # print(data)
    # print('\n')
    # print('---------')
    # exit()
    query = "INSERT INTO {0} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(table_list[index])
    cursor.executemany(query , data)
    index +=1
    data = []
    connection.commit()
