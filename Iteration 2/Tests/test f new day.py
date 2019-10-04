#Import everything from tkinter module
from tkinter import *

#To initialize Tkinter, we have to create a Tk root widget
#which is a window with a title bar
window = Tk()
window.title('Stock Market')
window.geometry('{}x{}'.format(1000, 1000))
window.wm_iconbitmap('icon.ico')

finishDay = True

def done_check():
    global finishDay
    finishDay = True
    print('ur done')
    
def day_change():
    global finishDay
    if finishDay == True:
        print('hi')
        print(finishDay)
        finishDay = False
    else:
        print('click done first')

menubar = Menu(window)
filemenu = Menu(menubar,tearoff=0)

# add commands to menu
filemenu.add_command(label="Done?", command = done_check)
filemenu.add_command(label="New Day", command = day_change)
menubar.add_cascade(label="Day", menu=filemenu)
window.config(menu=menubar)

window.mainloop()
