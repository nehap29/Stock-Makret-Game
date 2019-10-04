from tkinter import *
from tkinter import ttk

import tkinter as tk

LARGE_FONT= ("Arial", 16)
SMALL_FONT= ("Arial", 12)


class LogIn():

    def LogInCheck(self):
        global actEntry
        global pinEntry

        act = "james"
        pin = "Python123"

        actNum = actEntry.get()
        pinNum = pinEntry.get()

        print("FUNCTION RUN")
        if actNum == act and pinNum == pin:
            print("CORRECT")
            self.show_frame(StartPage)
        elif actNum != act or pinNum != pin: 
            print("INCORRECT")
            self.show_frame(LogIn)

    def __init__(self):

        global actEntry
        global pinEntry

        tk.Frame.__init__(self)

        logLabel = ttk.Label(self, text = "Login With Your Username and Password", font = LARGE_FONT)
        logLabel.pack(side = TOP, anchor = N, expand = YES)


        actLabel = Label(self, text = 'Username:')
        actEntry = Entry(self)

        pinLabel = Label(self, text = 'Password: ')
        pinEntry = Entry(self, show ="*")

        actLabel.pack(pady =10, padx = 10, side = TOP, anchor = N)
        pinLabel.pack(pady =5, padx = 10, side = TOP, anchor  = S)

        actEntry.pack(pady =10, padx = 10, side = TOP, anchor = N)
        pinEntry.pack(pady =5, padx = 10, side = TOP, anchor  = S)

        #  runs the 'LoginCheck' function

        logInButton = tk.Button(self, text = "Login",
                                 command = self.LogInCheck)
        logInButton.pack(side = TOP, anchor = S)

        quitButton = tk.Button(self, text = "Quit", command = quit)
        quitButton.pack(side = BOTTOM, anchor = S)


if __name__ == "__main__":
    app = LogIn()
    app.mainloop()
