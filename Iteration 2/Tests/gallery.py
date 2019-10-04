
from tkinter import *

root = Tk()
root.title("RandomizedPic")

img = ['0.gif', '1.gif', '2.gif', '3.gif']#,'4.gif', '5.gif', '6.gif', '7.gif']


class GUI:

    i = 0
    def __init__(self, root):
        global img
        frame = Frame(root)

        frame.pack(side = TOP)
        frame2 = Frame(root)
        frame2.pack(side = BOTTOM)

        self.igm = PhotoImage(file=img[self.i])
        pic = Button(frame, image=self.igm)
        pic.pack(side = BOTTOM)

        
        def clear():
            list = frame.pack_slaves()
            for l in list:
                l.destroy()
        def back_btn(*args):
            print(self.i)
            if self.i > 1:
                clear()
                self.i = self.i - 1
                print(self.i)
                img_update()
            else: 
                self.back.config(state='disabled')
                self.next.config(state='active')
        def next_btn(*args):
            clear()
            print(self.i)
            if self.i < (len(img)):
                self.i = self.i + 1
                print(self.i)
                img_update()
            else:
                self.next.config(state='disabled')
                self.back.config(state='active')
        def img_update():
            self.igm = PhotoImage(file=img[self.i])
            pic = Button(frame, image=self.igm)
            pic.pack(side = BOTTOM)


        self.back = Button(frame2,text = 'Back',command = back_btn)
        self.back.pack(side = LEFT)
        self.next = Button(frame2,text = 'Next',command = next_btn)
        self.next.pack(side = RIGHT)


gui = GUI(root)
root.mainloop()
