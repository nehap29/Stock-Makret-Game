#######################
#Stop frames resizing : pack_propagate(False) or grid_propagate(False)


#########################

#Import everything from tkinter module
from tkinter import *

#To initialize Tkinter, we have to create a Tk root widget
#which is a window with a title bar
window = Tk()
window.title('Stock Market')
window.geometry('{}x{}'.format(1000, 1000))
window.wm_iconbitmap('icon.ico')

#so that a GUI object can be made that deals with all the visual side
class GUI:
    def __init__(self, window):

        #A Frame is a container widget which is placed inside a window,
        #which can have its own border and background
        #it is used to group related widgets together in an application’s layout.
        assets_frame = Frame(window,bg='cyan',width=200, height=1000, pady=3)
        graph_frame = Frame(window,bg='green',width=800, height=500, pady=3)
        company_frame = Frame(window,bg='red',width=800, height=200, pady=3)
        bank_frame = Frame(window,bg='orange',width=300, height=300, pady=3)
        news_frame = Frame(window,bg='blue',width=500, height=300, pady=3)

        #Layout of the main frames
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        assets_frame.grid(column = 0,columnspan =2, rowspan = 10)
        graph_frame.grid(column =2, row= 0, rowspan = 4, columnspan = 8)
        company_frame.grid(column = 2,row = 5,rowspan = 2, columnspan = 8)
        news_frame.grid(column = 2, row =7, rowspan = 3, columnspan = 5)
        bank_frame.grid(column= 7, row = 7 , columnspan = 3 , rowspan = 3)

        #widgets for comapany_frame
        company_frame.grid_propagate(False)
        self.button = Button(company_frame,text = 'company',bg='#197796', fg='white')
        self.button.grid(column = 0, row = 0)
        self.button = Button(company_frame,text = 'company')
        self.button.grid(column = 1, row = 0)
        self.button = Button(company_frame,text = 'company')
        self.button.grid(column = 2, row = 0)
        self.button = Button(company_frame,text = 'company')
        self.button.grid(column = 0, row = 1)
        self.button = Button(company_frame,text = 'company')
        self.button.grid(column = 1, row = 1)
        self.button = Button(company_frame,text = 'company')
        self.button.grid(column = 2, row = 1)


                
gui = GUI(window)
window.mainloop()


