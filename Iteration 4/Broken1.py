#######################
#Stop frames resizing : pack_propagate(False) or grid_propagate(False)


###########
##############


#Import everything from tkinter module
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
import hashlib

#To initialize Tkinter, we have to create a Tk root widget
#which is a window with a title bar
window = Tk()

#Initialising global variables

#Which user:
ID = '0'

#How much money the user has
money = 1000

#Difficulty chosen by the user 
level = 2

#What day the user is on
day = 0

#List of all the hints
img = ['0.gif', '1.gif', '2.gif', '3.gif',
       '4.gif', '5.gif', '6.gif', '7.gif',
       '8.gif', '9.gif', '10.gif', '11.gif']


#################################################################################


#LOGIN CLASS


#################################################################################

class LogIn(Frame):
    def __init__(self):
        super().__init__()
        self.user_label = Label(self, text="Username")
        self.user_entry = Entry(self)

        self.logbtn = Button(self, text="Login", command = self.login_check)
        self.user_label.grid(row=0, sticky=E)

        self.user_entry.grid(row=0, column=1)
        self.logbtn.grid(row = 5,columnspan=2)

        self.pass_label = Label(self, text="Password")
        self.pass_entry = Entry(self, show="*")
        self.pass_label.grid(row=3, sticky=E)
        self.pass_entry.grid(row=3, column=1)


        self.grid()


    def login_check(self):
        username = self.user_entry.get()
        found = DB.userexist(self,username)
        print(found)
        if found == True:
            LogIn.pass_enter(self,username)
        else:
            LogIn()

    def pass_enter(self,username):
        password = self.pass_entry.get()
        print('password entered:' , password)
        foundpass = DB.passexist(self,password,username)
        print(foundpass)
        if foundpass == True:
            tm.showinfo("Login", "Hiya Neha")
            window.title('Stock Market')
            window.geometry('{}x{}'.format(1000, 800))
            window.wm_iconbitmap('ICON.ico')
            DB.set_global(self,username)
            GUI(window,database)
            toplevel()
            



#################################################################################


#GUI CLASS


#################################################################################


#so that a GUI object can be made that deals with all the visual side
class GUI():
    #initialising the pointer - so that we can index img list full of images
    i = 0
##Everything see on the GUI
    def __init__(self, window, database):

        #A Frame is a container widget which is placed inside a window,
        #which can have its own border and background
        #it is used to group related widgets together in an application’s layout.
        self.assets_frame = Frame(window,bg='#0a561b',width=200, height=800, pady=3,highlightthickness=4, highlightbackground="#111")
        self.graph_frame = Frame(window,bg='#e15d03',width=800, height=300, pady=3,highlightthickness=4, highlightbackground="#111")
 
        self.company_frame = Frame(window,bg='#50871c',width=800, height=200, pady=5,padx =7,highlightthickness=4, highlightbackground="#111")
        self.bank_frame = Frame(window,bg='#117e34',width=300, height=300, pady=3,highlightthickness=4, highlightbackground="#111")
        self.news_frame = Frame(window,bg='#c52800',width=500, height=250, pady=3,highlightthickness=4, highlightbackground="#111")
        self.news_frame_btns = Frame(window,bg='#c52800',width=500, height=50, pady=3,highlightthickness=4, highlightbackground="#111")

##Initially setting the window into a grid structure
        #Layout of the main frames
        #window.grid_rowconfigure(0, weight=1)
        #window.grid_columnconfigure(0, weight=1)
        
        self.assets_frame.pack(side= LEFT, fill =Y)
        self.graph_frame.pack(side = TOP, fill=X)
        self.company_frame.pack(side = TOP, fill=X)
        self.bank_frame.pack(side= RIGHT)
        self.news_frame_btns.pack(side=TOP)
        self.news_frame.pack(side=BOTTOM)
        
##widgets for company_frame
        self.company_frame.grid_propagate(False)
        self.igm1 = PhotoImage(file="sellFOOD.gif")
        Button(self.company_frame, image=self.igm1,height=80, width= 122,command=lambda: self.sell(1)).grid(column = 0, row = 0)
        self.igm12 = PhotoImage(file="buyFOOD.gif")
        Button(self.company_frame, image=self.igm12,height=80, width=122,command=lambda: self.buy(1)).grid(column = 1, row = 0)
        self.igm2 = PhotoImage(file="sellHOTELS.gif")
        Button(self.company_frame, image=self.igm2,height=80, width= 122,command=lambda: self.sell(2)).grid(column = 2, row = 0)
        self.igm22 = PhotoImage(file="buyHOTELS.gif")
        Button(self.company_frame, image=self.igm22,height=80, width= 122,command=lambda: self.buy(2)).grid(column = 3, row = 0)
        self.igm3 = PhotoImage(file="sellTECH.gif")
        Button(self.company_frame, image=self.igm3,height=80, width= 122,command=lambda: self.sell(3)).grid(column = 4, row = 0)
        self.igm32 = PhotoImage(file="buyTECH.gif")
        Button(self.company_frame, image=self.igm32,height=80, width= 122,command=lambda: self.buy(3)).grid(column = 5, row = 0)
        self.igm4 = PhotoImage(file="sellHEALTH.gif")
        Button(self.company_frame, image=self.igm4,height=80, width= 122,command=lambda: self.sell(4)).grid(column = 0, row = 1)
        self.igm42 = PhotoImage(file="buyHEALTH.gif")
        Button(self.company_frame, image=self.igm42,height=80, width= 122,command=lambda: self.buy(4)).grid(column = 1, row = 1)
        self.igm5 = PhotoImage(file="sellCAR.gif")
        Button(self.company_frame, image=self.igm5,height=80, width= 122,command=lambda: self.sell(5)).grid(column = 2, row = 1)
        self.igm52 = PhotoImage(file="buyCAR.gif")
        Button(self.company_frame, image=self.igm52,height=80, width= 122,command=lambda: self.buy(5)).grid(column = 3, row = 1)
        self.igm6 = PhotoImage(file="sellOIL.gif")
        Button(self.company_frame, image=self.igm6,height=80, width= 122,command=lambda: self.sell(6)).grid(column = 4, row = 1)
        self.igm62 = PhotoImage(file="buyOIL.gif")
        Button(self.company_frame, image=self.igm62,height=80, width= 122,command=lambda: self.buy(6)).grid(column = 5, row = 1)


##widgets for assets frame
        self.assets_frame.pack_propagate(False)
        v = StringVar()
        Label(self.assets_frame, textvariable=v,bg='#0a561b',fg= 'white').pack(side=TOP)
        #Requests database class to load the users current assets
        numbers = Main.info4assets(self)
        print(numbers)
        quote = ('FOOD \n' + str(numbers[0]) + '\nHOTELS \n' + str(numbers[1]) + '\nTECH \n' + str(numbers[2]) +
                 '\nHEALTH \n' + str(numbers[3]) + '\nCAR \n' + str(numbers[4]) + '\nOIL \n' + str(numbers[5]))
        v.set(quote)
        Textbox = Text(self.assets_frame)
        Textbox.pack(side=LEFT, fill=Y)
        textbox_message= ('Notes:\n')
        Textbox.insert(END, textbox_message)
##widgets for graph_frame


##widgets for news_frame
        #sets the two frames - the button frame and picture frame
        self.news_frame_btns.pack_propagate(False)
        self.news_frame.pack_propagate(False)
        #sets teh first image 
        self.igm = PhotoImage(file=img[self.i])
        pic = Button(self.news_frame, image=self.igm)
        pic.pack(side = BOTTOM)

        #buttons that allow user to change viewed image  
        self.back = Button(self.news_frame_btns,text = 'Back',command = self.back_btn)
        self.back.pack(side = LEFT)
        self.next = Button(self.news_frame_btns,text = 'Next',command = self.next_btn)
        self.next.pack(side = RIGHT)
        self.current = Button(self.news_frame_btns,text = 'Current',command = self.present)
        self.current.pack()

##widgets for bank_frame
        self.bank_frame.pack_propagate(False)
        v = StringVar()
        Label(self.bank_frame, textvariable=v,bg='#117e34',fg= 'white').pack()
        quote = ('you have')
        v.set(quote)
        r = StringVar()
        Label(self.bank_frame, textvariable=r,bg='#117e34',fg= 'white').pack()
        quote = (money)
        r.set(quote)
        
##The menu bar so the user can change Days
        menubar = Menu(window)
        filemenu = Menu(menubar,tearoff=0)

        #add commands to menu
        filemenu.add_command(label="Done?", command = self.done_check)
        filemenu.add_command(label="New Day", command = self.day_pass)
        menubar.add_cascade(label="Day", menu=filemenu)
        window.config(menu=menubar)

##functions for changing the day - functionallity for the menu buttons
    #checks user is done with the curretn day
    def done_check(self):
        self.finishDay = True
        print('ur done')
    #changes the day
    def day_pass(self):
        if self.finishDay == True:
            Main.day_change(self)
        else:
            print('click done first')
            
#Sends the name of the company button in the company_frame to the Main class
#Calls functions to update money in the bank 
    def sell(self,company):
        self.clear_bank()
        Main.SellAsset(self,company)
        self.setup_bank()
    def buy(self,company):
        self.clear_bank()
        Main.BuyAsset(self,company)
        self.setup_bank()
    def ClearAndAssets(self,owned):
        list = self.assets_frame.pack_slaves()
        for l in list:
            l.destroy()
        v = StringVar()
        Label(self.assets_frame, textvariable=v,bg='#0a561b',fg= 'white').pack()
        #Requests database class to load the users current assets
        quote = ('FOOD \n' + str(owned[0]) + '\nHOTELS \n' + str(owned[1]) + '\nTECH \n' + str(owned[2]) +
                 '\nHEALTH \n' + str(owned[3]) + '\nCAR \n' + str(owned[4]) + '\nOIL \n' + str(owned[5]))
        v.set(quote)
##FUNCTION FOR BANK
    def setup_bank(self):
        self.bank_frame.pack_propagate(False)
        v = StringVar()
        Label(self.bank_frame, textvariable=v,bg='#117e34',fg= 'white').pack()
        quote = ('you have')
        v.set(quote)
        r = StringVar()
        Label(self.bank_frame, textvariable=r,bg='#117e34',fg= 'white').pack()
        quote = (money)
        r.set(quote)

    def clear_bank(self):
        list = self.bank_frame.pack_slaves()
        for l in list:
            l.destroy()    
##Functions for the news_frame
    #CLEARS FRAME FOR ALL FRAMES THAT NEED UPDATING AFTER AN EVENT 
    def clear_news(self):
        list = self.news_frame.pack_slaves()
        for l in list:
            l.destroy()
    #decrements the pointer
    def back_btn(self):
        print(self.i)
        if self.i >= 1:
            self.clear_news()
            self.i = self.i - level
            print(self.i)
            self.img_update()
        #so image does not change when they are looking at the first picture
        else:
            self.i = 0
            #self.back.config(state='disabled')
            #self.next.config(state='active')
    #increments pointer
    def next_btn(self):
        self.clear_news()
        print(self.i)
        if self.i < ((day//level)*level) and (self.i + level)<=(len(img)-1):
            self.i = self.i + level
            print(self.i)
        self.img_update()
        #else:
            #self.next.config(state='disabled')
            #self.back.config(state='active')
    #updates the displayed image when called by button functions back and next
    def img_update(self):
        self.igm = PhotoImage(file=img[self.i])
        pic = Button(self.news_frame, image=self.igm)
        pic.pack(side = BOTTOM)
    #moves the pointer so that the image displayed is the hint for the current day
    def present(self):
        self.clear_news()
        print(self.i)
        if (day-1) * level <= (len(img)-1) and (day%level == 0):
            self.i = (day-1) * level
            self.igm = PhotoImage(file=img[self.i])
            pic = Button(self.news_frame, image=self.igm)
            pic.pack(side = BOTTOM)
        else:
            self.i = (day//level)*level
            self.igm = PhotoImage(file=img[self.i])
            pic = Button(self.news_frame, image=self.igm)
            pic.pack(side = BOTTOM)


#################################################################################


#MAIN CLASS


#################################################################################


##Communicates between DB amd GUI classes
##as per the Model View Controller development style
class Main:
##Initalising an object of the database class
    def __init__(self):
        self.z = 9
    
#initially gets the number owned assets from the database
    def info4assets(self):
        numbers = DB.show_assets(self)
        print(numbers)
        #returns the information in a 2D array stip dwon to normal array
        self.no_owned = []
        for i in range (0,len(numbers)):
            self.no_owned.append(numbers[i][2])
        return(self.no_owned)

##Changed the global variable day for the whole program
    def day_change(self):
        global day
        global money
        day = day +1
        print(day)
        #Adding profit
        records = DB.price_change()
        for i in range (0,7):
            change = (records[(i*2)+1][0])-(records[i*2][0])
            money = money + (change*self.no_owned[i])
            print(money)
        print(self.no_owned)
        #Refreshing the bank
        GUI.clear_bank(self)
        GUI.setup_bank(self)

##Takes the comapny button pressed in the GUI
##Decrements the number owned list and updates the gui
    def SellAsset(self,company):
        global money
        earned = DB.price(self,company)
        money = money + earned[0][0]
        print(money)
        print(self.no_owned)
        self.no_owned[company-1] = self.no_owned[company-1] -1
        GUI.ClearAndAssets(self,self.no_owned)

##Takes the comapny button pressed in the GUI
##Increments the number owned list and updates the gui
    def BuyAsset(self,company):
        global money
        earned = DB.price(self,company)
        money = money - earned[0][0]
        print(money)
        self.no_owned[company-1] = self.no_owned[company-1] + 1
        GUI.ClearAndAssets(self,self.no_owned)


#################################################################################


#DB CLASS


#################################################################################



##Handels all databse interaction
class DB:
    import sqlite3
##Initalising an object of the database class
    def __init__(self):
        self.u = 9
    def set_global(self,username):
        global ID
        global day
        global level
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        command = ('SELECT username FROM user_info')
        c.execute(command)
        user_list = c.fetchall()
        for i in range (0,len(user_list)):
            if (user_list[i][0]) == username:
                command = ("SELECT * FROM user_info WHERE username = '"+ username +"'")
                c.execute(command)
                info = c.fetchall()
                ID =info[0][0]
                level = int(info[0][3])
                day = int(info[0][4])
        
##Collects the Assets for the user from the database 
    def show_assets(self):
        global money
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        ID = '1'
        command = ("SELECT * FROM assets WHERE user_ID ='"+ ID +"'")
        c.execute(command)
        got_numbers = c.fetchall()
        money = got_numbers[6][2]
        return(got_numbers)


##Collects the users chosen level of difficulty from the databse
    def difficulty():
        global level
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        c.execute('SELECT difficulty FROM assets WHERE user_ID = 1')
        level = c.fetchall()

##Collects the Assets for the user from the database 
    def price(self,company):
        global day
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        command = ('SELECT price FROM stock_price WHERE company_ID = ' + str(company) + ' AND dayNo ='+ str(day))
        c.execute(command)
        return(c.fetchall())
    
    def userexist(self,username):
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        command = ('SELECT username FROM user_info')
        c.execute(command)
        user_list = c.fetchall()
        found = False
        for i in range (0,len(user_list)):
            if (user_list[i][0]) == username:
                found = True
        return(found)

    def passexist(self,password,username):
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        command = ("SELECT password FROM user_info WHERE username = '"+ username +"'")
        c.execute(command)
        pass_returned = c.fetchall()
        password = hashlib.md5(password.encode())
        found_pass = pass_returned[0][0]
        found_pass = hashlib.md5(found_pass.encode())
        foundpass = False
        if found_pass.hexdigest() == password.hexdigest():
            foundpass = True
        return(foundpass)
        
#code that will bring up the points that need to be plotted for each comapny day by dy
    def price_change():
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        command = ("SELECT price,dayNo,company_ID FROM stock_price WHERE dayNo = '"+ str(day-1) +"'OR dayNo = '"+ str(day) +"'")
        c.execute(command)
        records = c.fetchall()
        return(records)        

def graph_points():
    global day
    import sqlite3
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    coords = [[],[],[],[],[],[],[]]
    for i in range(0,7):
        command = ("SELECT price FROM stock_price WHERE company_ID = '"+ str(i+1) +"'")
        c.execute(command)
        all_prices = c.fetchall()
        for j in range(0,day+1):
            #setting y coordinates for each comapny
            coords[i].append(all_prices[j])
    return(coords)

def toplevel():
    top = Toplevel()
    top.title('Optimized Map')
    top.wm_geometry("794x370")
    optimized_canvas = Canvas(top)
    optimized_canvas.pack(fill=BOTH, expand=1)
    optimized_image = optimized_canvas.create_image(0, 0, anchor=NW)
    coords = graph_points()
    import matplotlib.pyplot as plt
    plt.plot(coords[0],label='comp1')
    plt.plot(coords[1],label='comp2')
    plt.plot(coords[2],label='comp3')
    plt.plot(coords[3],label='comp4')
    plt.plot(coords[4],label='comp5')
    plt.plot(coords[5],label='comp6')
    plt.plot(coords[6],label='comp7')


    plt.title('STOCK MARKET')
    plt.ylabel('price')
    plt.xlabel('day')
    plt.legend()
    plt.show()

database = DB()
login= LogIn()
window.mainloop()

