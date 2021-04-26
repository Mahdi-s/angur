import sqlite3

#create database
connection = sqlite3.connect('stocks.db')
#create cursor instance
cursor = connection.cursor()
#create tables
cursor.execute("""CREATE TABLE comapny (
    ticker text,
    company_name text,
    company_industry text
)""")
cursor.execute("""CREATE TABLE annual_income_statement_amazon (
    ticker text,
    release_date text,
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
    ticker text,
    release_date text,
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
    ticker text,
    release_date text,
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
    ticker text,
    release_date text,
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
    ticker text,
    release_date text,
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
    ticker text,
    release_date text,
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
    ticker text,
    release_date text,
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
    ticker text,
    release_date text,
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
    ticker text,
    release_date text,
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
    ticker text,
    release_date text,
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
    ticker text,
    price_to_book real,
    price_to_earing real,
    divident_yield real
)""")
cursor.execute("""CREATE TABLE market_historical_data_amazon (
    ticker text,
    open_price real,
    high_price real,
    low_price real,
    close_price real,
    adjusted_close_price real,
    volume_traded integer
)""")
cursor.execute("""CREATE TABLE market_historical_data_bestbuy (
    ticker text,
    open_price real,
    high_price real,
    low_price real,
    close_price real,
    adjusted_close_price real,
    volume_traded integer
)""")
cursor.execute("""CREATE TABLE market_historical_data_facebook (
    ticker text,
    open_price real,
    high_price real,
    low_price real,
    close_price real,
    adjusted_close_price real,
    volume_traded integer
)""")
cursor.execute("""CREATE TABLE market_historical_data_tesla (
    ticker text,
    open_price real,
    high_price real,
    low_price real,
    close_price real,
    adjusted_close_price real,
    volume_traded integer
)""")
cursor.execute("""CREATE TABLE market_historical_data_alphabet (
    ticker text,
    open_price real,
    high_price real,
    low_price real,
    close_price real,
    adjusted_close_price real,
    volume_traded integer
)""")
cursor.execute("""CREATE TABLE market_historical_data_apple (
    ticker text,
    open_price real,
    high_price real,
    low_price real,
    close_price real,
    adjusted_close_price real,
    volume_traded integer
)""")
cursor.execute("""CREATE TABLE market_historical_data_boeing (
    ticker text,
    open_price real,
    high_price real,
    low_price real,
    close_price real,
    adjusted_close_price real,
    volume_traded integer
)""")
cursor.execute("""CREATE TABLE market_historical_data_twitter (
    ticker text,
    open_price real,
    high_price real,
    low_price real,
    close_price real,
    adjusted_close_price real,
    volume_traded integer
)""")
cursor.execute("""CREATE TABLE market_historical_data_palantir (
    ticker text,
    open_price real,
    high_price real,
    low_price real,
    close_price real,
    adjusted_close_price real,
    volume_traded integer
)""")
cursor.execute("""CREATE TABLE market_historical_data_walmart (
    ticker text,
    open_price real,
    high_price real,
    low_price real,
    close_price real,
    adjusted_close_price real,
    volume_traded integer
)""")
cursor.execute("""CREATE TABLE article_list (
    ticker text,
    release_date text,
    url text,
    publisher text,
    pros text,
    cons text
)""")
cursor.execute("""CREATE TABLE user (
    user_email text,
    sign_on_data text,
    opt_out text
)""")
cursor.execute("""CREATE TABLE user_communication (
    user_email text,
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
