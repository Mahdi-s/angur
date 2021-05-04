import sqlite3

#create database
connection = sqlite3.connect('stocks.db')
#create cursor instance
cursor = connection.cursor()
#create tables
cursor.execute("""CREATE TABLE comapny (
    ticker text PRIMARY KEY,
    company_name text,
    company_industry text
)""")
cursor.execute("""CREATE TABLE annual_income_statement_amazon (
    year integer PRIMARY KEY,
    revenue real,
    cost_of_goods_sold real,
    gross_profit real,
    rand_expenses real,
    sg_a_expenses real,
    operating_expenses real,
    operating_income real,
    pre_tax_income real,
    income_taxes real,
    income_after_taxes real,
    income_from_continuous_operations real,
    net_income real,
    ebitda real,
    ebit real,
    basic_shares_outstanding real,
    shares_outstanding real,
    basic_eps real,
    eps_earning_per_share real
)""")
cursor.execute("""CREATE TABLE annual_income_statement_bestbuy (
    year integer PRIMARY KEY,
    revenue real,
    cost_of_goods_sold real,
    gross_profit real,
    rand_expenses real,
    sg_a_expenses real,
    operating_expenses real,
    operating_income real,
    pre_tax_income real,
    income_taxes real,
    income_after_taxes real,
    income_from_continuous_operations real,
    net_income real,
    ebitda real,
    ebit real,
    basic_shares_outstanding real,
    shares_outstanding real,
    basic_eps real,
    eps_earning_per_share real
)""")
cursor.execute("""CREATE TABLE annual_income_statement_facebook (
    year integer PRIMARY KEY,
    revenue real,
    cost_of_goods_sold real,
    gross_profit real,
    rand_expenses real,
    sg_a_expenses real,
    operating_expenses real,
    operating_income real,
    pre_tax_income real,
    income_taxes real,
    income_after_taxes real,
    income_from_continuous_operations real,
    net_income real,
    ebitda real,
    ebit real,
    basic_shares_outstanding real,
    shares_outstanding real,
    basic_eps real,
    eps_earning_per_share real
)""")
cursor.execute("""CREATE TABLE annual_income_statement_tesla (
    year integer PRIMARY KEY,
    revenue real,
    cost_of_goods_sold real,
    gross_profit real,
    rand_expenses real,
    sg_a_expenses real,
    operating_expenses real,
    operating_income real,
    pre_tax_income real,
    income_taxes real,
    income_after_taxes real,
    income_from_continuous_operations real,
    net_income real,
    ebitda real,
    ebit real,
    basic_shares_outstanding real,
    shares_outstanding real,
    basic_eps real,
    eps_earning_per_share real
)""")
cursor.execute("""CREATE TABLE annual_income_statement_alphabet (
    year integer PRIMARY KEY,
    revenue real,
    cost_of_goods_sold real,
    gross_profit real,
    rand_expenses real,
    sg_a_expenses real,
    operating_expenses real,
    operating_income real,
    pre_tax_income real,
    income_taxes real,
    income_after_taxes real,
    income_from_continuous_operations real,
    net_income real,
    ebitda real,
    ebit real,
    basic_shares_outstanding real,
    shares_outstanding real,
    basic_eps real,
    eps_earning_per_share real
)""")
cursor.execute("""CREATE TABLE annual_income_statement_apple (
    year integer PRIMARY KEY,
    revenue real,
    cost_of_goods_sold real,
    gross_profit real,
    rand_expenses real,
    sg_a_expenses real,
    operating_expenses real,
    operating_income real,
    pre_tax_income real,
    income_taxes real,
    income_after_taxes real,
    income_from_continuous_operations real,
    net_income real,
    ebitda real,
    ebit real,
    basic_shares_outstanding real,
    shares_outstanding real,
    basic_eps real,
    eps_earning_per_share real
)""")
cursor.execute("""CREATE TABLE annual_income_statement_boeing (
    year integer PRIMARY KEY,
    revenue real,
    cost_of_goods_sold real,
    gross_profit real,
    rand_expenses real,
    sg_a_expenses real,
    operating_expenses real,
    operating_income real,
    pre_tax_income real,
    income_taxes real,
    income_after_taxes real,
    income_from_continuous_operations real,
    net_income real,
    ebitda real,
    ebit real,
    basic_shares_outstanding real,
    shares_outstanding real,
    basic_eps real,
    eps_earning_per_share real
)""")
cursor.execute("""CREATE TABLE annual_income_statement_twitter (
    year integer PRIMARY KEY,
    revenue real,
    cost_of_goods_sold real,
    gross_profit real,
    rand_expenses real,
    sg_a_expenses real,
    operating_expenses real,
    operating_income real,
    pre_tax_income real,
    income_taxes real,
    income_after_taxes real,
    income_from_continuous_operations real,
    net_income real,
    ebitda real,
    ebit real,
    basic_shares_outstanding real,
    shares_outstanding real,
    basic_eps real,
    eps_earning_per_share real
)""")
cursor.execute("""CREATE TABLE annual_income_statement_palantir (
    year integer PRIMARY KEY,
    revenue real,
    cost_of_goods_sold real,
    gross_profit real,
    rand_expenses real,
    sg_a_expenses real,
    operating_expenses real,
    operating_income real,
    pre_tax_income real,
    income_taxes real,
    income_after_taxes real,
    income_from_continuous_operations real,
    net_income real,
    ebitda real,
    ebit real,
    basic_shares_outstanding real,
    shares_outstanding real,
    basic_eps real,
    eps_earning_per_share real
)""")
cursor.execute("""CREATE TABLE annual_income_statement_walmart (
    year integer PRIMARY KEY,
    revenue real,
    cost_of_goods_sold real,
    gross_profit real,
    rand_expenses real,
    sg_a_expenses real,
    operating_expenses real,
    operating_income real,
    pre_tax_income real,
    income_taxes real,
    income_after_taxes real,
    income_from_continuous_operations real,
    net_income real,
    ebitda real,
    ebit real,
    basic_shares_outstanding real,
    shares_outstanding real,
    basic_eps real,
    eps_earning_per_share real
)""")
cursor.execute("""CREATE TABLE calculated_ratios (
    ticker text PRIMARY KEY,
    price_to_book real,
    price_to_earing real,
    divident_yield real
)""")
cursor.execute("""CREATE TABLE market_historical_data_amazon (
    date text PRIMARY KEY,
    high_price real,
    low_price real,
    open_price real,
    close_price real,
    volume_traded integer,
    adjusted_close_price real
)""")
cursor.execute("""CREATE TABLE market_historical_data_bestbuy (
    date text PRIMARY KEY,
    high_price real,
    low_price real,
    open_price real,
    close_price real,
    volume_traded integer,
    adjusted_close_price real
)""")
cursor.execute("""CREATE TABLE market_historical_data_facebook (
    date text PRIMARY KEY,
    high_price real,
    low_price real,
    open_price real,
    close_price real,
    volume_traded integer,
    adjusted_close_price real
)""")
cursor.execute("""CREATE TABLE market_historical_data_tesla (
    date text PRIMARY KEY,
    high_price real,
    low_price real,
    open_price real,
    close_price real,
    volume_traded integer,
    adjusted_close_price real
)""")
cursor.execute("""CREATE TABLE market_historical_data_alphabet (
    date text PRIMARY KEY,
    high_price real,
    low_price real,
    open_price real,
    close_price real,
    volume_traded integer,
    adjusted_close_price real
)""")
cursor.execute("""CREATE TABLE market_historical_data_apple (
    date text PRIMARY KEY,
    high_price real,
    low_price real,
    open_price real,
    close_price real,
    volume_traded integer,
    adjusted_close_price real
)""")
cursor.execute("""CREATE TABLE market_historical_data_boeing (
    date text PRIMARY KEY,
    high_price real,
    low_price real,
    open_price real,
    close_price real,
    volume_traded integer,
    adjusted_close_price real
)""")
cursor.execute("""CREATE TABLE market_historical_data_twitter (
    date text PRIMARY KEY,
    high_price real,
    low_price real,
    open_price real,
    close_price real,
    volume_traded integer,
    adjusted_close_price real
)""")
cursor.execute("""CREATE TABLE market_historical_data_palantir (
    date text PRIMARY KEY,
    high_price real,
    low_price real,
    open_price real,
    close_price real,
    volume_traded integer,
    adjusted_close_price real
)""")
cursor.execute("""CREATE TABLE market_historical_data_walmart (
    date text PRIMARY KEY,
    high_price real,
    low_price real,
    open_price real,
    close_price real,
    volume_traded integer,
    adjusted_close_price real
)""")
cursor.execute("""CREATE TABLE article_list (
    comapany text,
    url text
)""")
cursor.execute("""CREATE TABLE user (
    user_email text PRIMARY KEY,
    sign_on_data text,
    opt_out text
)""")
cursor.execute("""CREATE TABLE user_communication (
    user_email text PRIMARY KEY,
    subject text,
    message text,
    date_stamp text
)""")
cursor.execute("""CREATE TABLE user_portfolio (
    user_email text,
    ticker_list text
)""")



#commit commads
connection.commit()
#close connection
connection.close()
