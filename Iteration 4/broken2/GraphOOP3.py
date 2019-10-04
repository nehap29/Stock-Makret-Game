
#Import everything from tkinter module
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
import hashlib
import matplotlib.pyplot as plt


def draw(day):
        ##widgets for graph_frame
        coords = graph_points(day)
        plt.plot(coords[0],label='comp1')
        plt.plot(coords[1],label='comp2')
        plt.plot(coords[2],label='comp3')
        plt.plot(coords[3],label='comp4')
        plt.plot(coords[4],label='comp5')
        plt.plot(coords[5],label='comp6')
        plt.plot(coords[6],label='comp7')

        plt.title('STOCK MARKET')
        plt.ylabel('price')
        plt.xlabel('day')
        plt.legend()
        plt.show()



#code that will bring up the points that need to be plotted for each comapny day by dy
def graph_points(day):
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



