import sqlite3
import csv
import pandas as pd
import urllib.request
import re
# #create database
# connection = sqlite3.connect('stocks.db')
# #create cursor instance
# c = connection.cursor()
#
#
#
# c.execute("SELECT year , revenue FROM annual_income_statement_apple")
# #c.execute("SELECT * FROM annual_income_statement_apple")
#
# print(c.fetchall())
# connection.commit()
def articles(searchTerm):
    NumberofArticles =3
    url="https://news.search.yahoo.com/search?p="+searchTerm
    link = urllib.request.urlopen(url)
    htmlbytes = link.read()
    html = htmlbytes.decode("utf-8")
    link.close()
    arr=[]
    results=re.findall("\"https:\/\/[^\"]+\" referrerpolicy=\"origin\"", html)
    print(results)
    #removing irrelevent links
    #print(results)
    print('testttt')
    for string in results:
        if not(string.endswith("png\"")):
            arr.append(string)
    #removing duplicate links
    arr=list(dict.fromkeys(arr))
    News=[]
    #condensing links into properlly formatted links to news articles
    for string in arr:
        News.append(string[1:len(string)-25])
    #condensing the array down to NumberofArticles: this wont reduce the array if the number is greater then the size News[]
    releventNews=[]
    i=0
    #print(News)
    while len(releventNews)<NumberofArticles:
        releventNews.append(News[i])
        i+=1
    return releventNews




arts = articles('google')

for a in arts:
    print(a)
