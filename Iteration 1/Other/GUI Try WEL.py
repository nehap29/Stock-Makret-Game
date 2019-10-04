import tkinter as TK  # otherwise you import lots of names and you know not what they all are

#def callback():
#    print ("called the callback!")

class App:

  def __init__(self):
    
    self.master = TK.Tk()
    self.master.title('Hello')
    self.master.wm_iconbitmap('favicon.ico')
    
    frame = TK.Frame(self.master)
    frame.pack() # pack frame inside master - NB will only be as big as necessary to fit whatever is inside
    self.button = TK.Button(frame, 
                         text="QUIT", fg="red",
                         command=self.quit)
    self.button.grid(row=1, column=1) # grid button inside frame
    self.slogan = TK.Button(frame,
                         text="Hello",
                         command=self.write_slogan)
    self.slogan.grid(row=0, column=0) # grid button inside frame
    
  def run(self):
    self.master.mainloop()

  def quit(self):
    self.master.destroy()
    
  def write_slogan(self):
    print("Hi")

#window = Tk()
#window.title('Hello')
#window.wm_iconbitmap('favicon.ico')

# create a menu

#menu = Menu(window)
app = App()
app.run()
#window.mainloop()
#window.config(menu=menu)



#filemenu = Menu(menu)
#menu.add_cascade(label="File", menu=filemenu)
#filemenu.add_command(label="New", command=callback)
#helpmenu = Menu(menu)
#menu.add_cascade(label="Help", menu=helpmenu)
#helpmenu.add_command(label="About...", command=callback)

#mainloop()



