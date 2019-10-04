

from tkinter import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class App:
    def __init__(self, master):
        # Create a container
        frame = Frame(master)
        # Create 2 buttons
        self.button_left = Button(frame,text="Next Day",
                                        command=self.change_day)
        self.button_left.pack(side="left")
        coords = App.graph_points()
        fig = Figure()
        ax = fig.add_subplot(111)
        self.line, = ax.plot(coords[0],label='comp1')
        self.line, =ax.plot(coords[1],label='comp2')
        self.line, =ax.plot(coords[2],label='comp3')
        self.line, =ax.plot(coords[3],label='comp4')
        self.line, =ax.plot(coords[4],label='comp5')
        self.line, =ax.plot(coords[5],label='comp6')
        self.line, =ax.plot(coords[6],label='comp7')
        ax.legend()
        self.canvas = FigureCanvasTkAgg(fig,master=master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        frame.pack()


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


    def change_day(self):
        global day
        day = day+ 1
        print(day)
        root = Tk()
        app = App(root)
        root.mainloop()
        
day = int(input('Day:'))
root = Tk()
app = App(root)
root.mainloop()
