from tkinter import *
from tkinter import ttk

import tkinter as tk


Large_Font = ("Verdana", 18)
Small_Font = ("Verdana", 12)

act = '1234567'
pin = '1234'


class ATM(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "ATM Simulator")

        #tk.Tk.iconbitmap(self, default = "atm.ico")

        container = tk.Frame(self)
        container.pack(side = "top", fill ="both", expand =True)
        container.grid_rowconfigure(100, weight=1)
        container.grid_columnconfigure(100, weight=1)

        self.frames = {}

        for i in (LogIn):

            frame = i(container, self)
            self.frames[i] = frame 
            frame.grid(row= 100, column = 100, sticky= "nsew")

        self.show_frame(LogIn)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LogIn(tk.Frame):
    def __init__(self, parent, controller):

        global actEntry
        global pinEntry

        tk.Frame.__init__(self, parent)

        logLabel = ttk.Label(self, text = "Login With Your Account Number and Pin", font = Large_Font)
        logLabel.pack(side = TOP, anchor = N, expand = YES)


        actLabel = Label(self, text = 'Account Number:')
        pinLabel = Label(self, text = 'PIN Number: ')

        actEntry = Entry(self)
        pinEntry = Entry(self, show ="*")

        actLabel.pack(pady =10, padx = 10, side = TOP, anchor = N)
        pinLabel.pack(pady =5, padx = 10, side = TOP, anchor  = S)

        actEntry.pack(pady =10, padx = 10, side = TOP, anchor = N)
        pinEntry.pack(pady =5, padx = 10, side = TOP, anchor  = S)

        #  runs the 'LoginCheck' function

        logInButton = ttk.Button(self, text = "Enter",
                                 command = self.LogInCheck)
        logInButton.pack(side = TOP, anchor = S)

        quitButton = ttk.Button(self, text = "Quit", command = quit)
        quitButton.pack(side = BOTTOM, anchor = S)

    def LogInCheck(self):
        actNum = actEntry.get()
        pinNum = pinEntry.get()

        if actNum == act and pinNum == pin:
            return 
            self.show_frame(WelcomePage)
        else: 
            return
            self.show_frame(LogIn)



atm = ATM()
atm.mainloop()    
