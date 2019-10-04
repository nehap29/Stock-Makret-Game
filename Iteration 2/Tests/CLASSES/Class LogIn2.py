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
        else:
            tm.showerror("Login error", "Incorrect username")

login = LogIn(window)
window.mainloop()
