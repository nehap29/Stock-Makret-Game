import tkinter as tk
import tkinter.ttk as ttk
# Change all label backgrounds
def change_colour():
    c = user.get() #Get the entered text of the Entry widget
    for wid in widget_list:
        wid.configure(bg = c)

# Create GUI
root = tk.Tk()

tk.Label(root, text='Enter a colour').pack()

user = tk.Entry(root)
user.pack()

label_frame = tk.Frame(root)
label_frame.pack()

btn = tk.Button(root, text='Change Colour', command = change_colour)
btn.pack()

widget_list = [user, btn] # Add defined widgets to list

#Dynamicly create labels for example
for x in range(10): 
    lbl = tk.Label(label_frame, text='Label '+str(x))
    lbl.pack(side = tk.LEFT)
    widget_list.append(lbl) #Add widget object to list

root.mainloop()
