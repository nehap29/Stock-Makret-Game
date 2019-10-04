
import sqlite3

##Establishing connection between pyhton and SQlite databse
conn = sqlite3.connect('stock.db')
c = conn.cursor()


'''##Tests for ways to get data points for the graph
c.execute('SELECT * FROM stock_prices')
data = (c.fetchall())
print(data)
day = 1
for i in range(0,day+1):
    for j in range(i,len(data),30):
        print(data[j][2])


##Test for company frame
##A way to retrieve comapny ID for the company that has been bought/sold
c.execute('SELECT * FROM company')
print(c.fetchall())


##Test for Assets frame
#retrieves the amount the user owns of a particulat company
##SQL statement needs to include user_ID
##in order to find the spesific amount of a company owned by a specific user
c.execute('SELECT amount FROM assets WHERE company_ID = 1')
print(c.fetchall())
'''

##For the bank frame
##To get the price of a specific company on a specific day
c.execute('SELECT price FROM stock_price WHERE company_ID AND dayNo = 0')
print(c.fetchall())


















