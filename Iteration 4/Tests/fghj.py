import matplotlib.pyplot as plt
day = 7



def graph_points():
    global day
    import sqlite3
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    coords = [[],[],[],[],[],[],[]]
    for i in range(0,7):
        command = ("SELECT price FROM stock_price WHERE company_ID = '"+ str(i+1) +"'")
        c.execute(command)
        all_prices = c.fetchall()
        for j in range(0,day+1):
            #setting y coordinates for each comapny
            coords[i].append(all_prices[j])
    return(coords)



coords = graph_points()
plt.plot(coords[0])
plt.show()
