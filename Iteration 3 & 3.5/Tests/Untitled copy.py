
day = 7


import sqlite3

#connecting to the stored databse
conn = sqlite3.connect('stock.db')
c = conn.cursor()

#making a 2D array to store all the points for the graph
# index relates to company_ID, inner list is the list of points
coords = [[],[],[],[],[],[],[]]

#Making a loop so the databse is queried for the point one company at a time
for i in range(0,7):
    command = ("SELECT price FROM stock_price WHERE company_ID = '"+ str(i+1) +"'")
    c.execute(command)
    # stroing result of query as an identifier
    all_prices = c.fetchall()
    # Looping through the list whihc was returned by the query
    #Storing correct parts of all_prices into the correct index of coords 2D array
    for j in range(0,day+1):
        #setting y coordinates for each comapny
        coords[i].append(all_prices[j])
print(coords)


#imporint matplotlib library
import matplotlib.pyplot as plt

#plotting each liner for each comapny 
plt.plot(coords[0],label='comp1')
plt.plot(coords[1],label='comp2')
plt.plot(coords[2],label='comp3')
plt.plot(coords[3],label='comp4')
plt.plot(coords[4],label='comp5')
plt.plot(coords[5],label='comp6')
plt.plot(coords[6],label='comp7')

#graph title
plt.title('STOCK MARKET')
#axis labels 
plt.ylabel('price')
plt.xlabel('day')
#key to tell user which line relates to which company
plt.legend()

#display the graph in a window
plt.show()


