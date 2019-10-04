from tkinter import *
import tkinter.messagebox as tm
import hashlib

#Password set
correct_pass = input('Set: ')
correct_pass = hashlib.md5(correct_pass.encode())
print(correct_pass.hexdigest())

window = Tk()


class LogIn(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.user_label = Label(self, text="Username")
        self.pass_label = Label(self, text="Password")

        self.user_entry = Entry(self)
        self.pass_entry = Entry(self, show="*")

        self.logbtn = Button(self, text="Login", command = self.login_check)

        self.user_label.grid(row=0, sticky=E)
        self.pass_label.grid(row=1, sticky=E)
        self.user_entry.grid(row=0, column=1)
        self.pass_entry.grid(row=1, column=1)
        self.logbtn.grid(columnspan=2)
        
        self.pack()

    def login_check(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        password = hashlib.md5(password.encode())
        print('password entered:' , password.hexdigest())
        
        if username == "neha" and password.hexdigest() == correct_pass.hexdigest():
            tm.showinfo("Login", "Hiya Neha")
            GUI.__init__(self,window)
        else:
            tm.showerror("Login error", "Incorrect username")

class GUI:

##Everything see on the GUI
    def __init__(self, window):

        #A Frame is a container widget which is placed inside a window,
        #which can have its own border and background
        #it is used to group related widgets together in an application’s layout.
        self.assets_frame = Frame(window,bg='#0a561b',width=200, height=1000, pady=3,highlightthickness=4, highlightbackground="#111")
        self.graph_frame = Frame(window,bg='#e15d03',width=800, height=500, pady=3,highlightthickness=4, highlightbackground="#111")
        self.company_frame = Frame(window,bg='#50871c',width=800, height=200, pady=5,padx =7,highlightthickness=4, highlightbackground="#111")
        self.bank_frame = Frame(window,bg='#117e34',width=300, height=300, pady=3,highlightthickness=4, highlightbackground="#111")
        self.news_frame = Frame(window,bg='#c52800',width=500, height=250, pady=3,highlightthickness=4, highlightbackground="#111")
        self.news_frame_btns = Frame(window,bg='#c52800',width=500, height=50, pady=3,highlightthickness=4, highlightbackground="#111")

##Initially setting the window into a grid structure
        #Layout of the main frames
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.assets_frame.grid(column = 0,columnspan =2, rowspan = 10)
        self.graph_frame.grid(column =2, row= 0, rowspan = 4, columnspan = 8)
        self.company_frame.grid(column = 2,row = 5,rowspan = 2, columnspan = 8)
        self.news_frame.grid(column = 2, row =8, rowspan = 2, columnspan = 5)
        self.news_frame_btns.grid(column = 2,columnspan = 5,row=7)
        self.bank_frame.grid(column= 7, row = 7 , columnspan = 3 , rowspan = 3)
        

login = LogIn(window)
window.mainloop()
