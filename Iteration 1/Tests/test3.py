import tkinter
import Image, ImageTk
root = Tkinter.Tk()
label = Tkinter.Label(root)
def change_image(image):
    photoimage = ImageTk.PhotoImage(image)
    label.config(image=photoimage)
root.mainloop()
