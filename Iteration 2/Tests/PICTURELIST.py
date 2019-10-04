from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("RandomizedPic")

pics = [None,None,None,None]   #  This will be the list that will hold a reference to each of your PhotoImages.

def randp(*args):
    w = ['0.gif', '1.gif', '2.gif', '3.gif']
    random.shuffle(w)
    am = 1

    for k, i in enumerate(w):    # Enumerate provides an index for the pics list.
        pic = PhotoImage(file=i)
        pics[k] = pic      # Keep a reference to the PhotoImage in the list, so your PhotoImage does not get garbage-collected.
        ttk.Label(mainframe, image=pic).grid(column=am, row=0, sticky=(W, E))
        am+=1

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Do it", command=randp).grid(column=0, row=0, sticky=W)

root.bind('<Return>', randp)
root.mainloop()
