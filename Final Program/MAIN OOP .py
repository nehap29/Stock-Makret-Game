#######################
#Stop frames resizing : pack_propagate(False) or grid_propagate(False)


###########
##############


#Import everything from tkinter module
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
import hashlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

#To initialize Tkinter, we have to create a Tk root widget
#which is a window with a title bar
window = Tk()

#Initialising global variables

#Which user:
ID = '0'

#users money
money = 0

#How much money the user has gained from comound interest
interest_gain = 0

#Difficulty chosen by the user 
level = 0

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
        #tells the function that other functions can inherit the variables and methods from this function
        #this means i can send what ever the user inputs into the input box to other functions for validation
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
        global day
        password = self.pass_entry.get()
        print('password entered:' , password)
        foundpass = DB.passexist(self,password,username)
        print(foundpass)
        if foundpass == True:
            tm.showinfo("Login", "Hiya " + username)
            tm.showinfo("Instructions", "The GUI is made up of 7 sections:\n- Top left is the assets frame it will show you how much of each company you own\n- The orange area is a button you can press and a graph will pop up showing you the changes in stock price up until the current day you are on\n- The blue section is the Statistics frame, it will give you information about the changes of stocks from the previous day and the prices of the stocks on the current day, you must play one complete day and change the day for statistics to show\n- The purple section is an area for you to make notes \n- The black buttons are used to buy and sell stocks\n- The Section with tweets in it are hints that will advise you, they are riddles you must interpret, you can look at previous hints using the navigation buttons, the frequency of hints you receive is dependent on your difficulty\n- The bottom right frame is the bank, it will tell you how much money you have and the interest rates of the bank that day\n\nOnce you are done buying and selling for that day click the Day button at the very topo left of the screen, click done and then click new day and the screen will refresh")
            window.title('Stock Market')
            window.geometry('{}x{}'.format(1000, 800))
            window.wm_iconbitmap('ICON.ico')
            DB.set_global(self,username)
            GUI(window,database)



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
        self.assets_frame = Frame(window,bg='#0a561b',width=200, height=300,highlightthickness=4, highlightbackground="#111")
        self.notes_frame = Frame(window,bg='#0a561b',width=200, height=500,highlightthickness=4, highlightbackground="#111")
        self.graph_frame = Frame(window,bg='#e15d03',width=800, height=100, pady=3,highlightthickness=4, highlightbackground="#111")
        self.stats_frame = Frame(window,bg='#4A6E9B',width=800, height=200, pady=3,highlightthickness=4, highlightbackground="#111")
        self.company_frame = Frame(window,bg='#50871c',width=800, height=200, pady=5,padx =7,highlightthickness=4, highlightbackground="#111")
        self.bank_frame = Frame(window,bg='#117e34',width=300, height=300, pady=3,highlightthickness=4, highlightbackground="#111")
        self.news_frame = Frame(window,bg='#c52800',width=500, height=250, pady=3,highlightthickness=4, highlightbackground="#111")
        self.news_frame_btns = Frame(window,bg='#c52800',width=500, height=50, pady=3,highlightthickness=4, highlightbackground="#111")

##Initially setting the window into a grid structure
        #Layout of the main frames
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        
        self.assets_frame.grid(column = 0,columnspan =2,row=0,rowspan = 4)
        self.graph_frame.grid(column =2, row= 0,  columnspan = 8)
        self.stats_frame.grid(column =2, row= 1, rowspan = 3,  columnspan = 8)
        self.notes_frame.grid(column =0, row=5, rowspan = 6,  columnspan = 2)
        self.company_frame.grid(column = 2,row = 5,rowspan = 2, columnspan = 8)
        self.news_frame.grid(column = 2, row =8, rowspan = 2, columnspan = 5)
        self.news_frame_btns.grid(column = 2,columnspan = 5,row=7)
        self.bank_frame.grid(column= 7, row = 7 , columnspan = 3 , rowspan = 3)

        
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
        quote = ('ASSETS:\n\n\nFOOD \n' + str(numbers[0]) + '\nHOTELS \n' + str(numbers[1]) + '\nTECH \n' + str(numbers[2]) +
                 '\nHEALTH \n' + str(numbers[3]) + '\nCAR \n' + str(numbers[4]) + '\nOIL \n' + str(numbers[5]))
        v.set(quote)
##widgets for notes_frame
        self.notes_frame.pack_propagate(False)
        Textbox = Text(self.notes_frame,background="#482030",foreground='white',font='bold')
        Textbox.pack(side=LEFT, fill=Y)
        textbox_message= ('Notes:\n')
        Textbox.insert(END, textbox_message)
##widgets for graph_frame
        self.graph_frame.grid_propagate(False)
        #Graph button to open graph window
        self.igm100 = PhotoImage(file="graph_btn.gif")
        self.button1 = Button(self.graph_frame, text = 'Open Graph Window',image=self.igm100,command= self.new_window, anchor = 'center')
        self.button1.grid(row = 0,column = 0)
        #save button to save progress
        self.igm101 = PhotoImage(file="Save_btn.gif")
        self.button2 = Button(self.graph_frame, text = 'Save',image=self.igm101,command= Main.info4save(self))
        self.button2.grid(row = 0,column = 4)
        #done button to confirm before chaning day
        self.igm102 = PhotoImage(file="Done_btn.gif")
        self.button3 = Button(self.graph_frame, text = 'Done',image=self.igm102,command= self.done_check)
        self.button3.grid(row = 0,column = 2)
        #button to change day
        self.igm103 = PhotoImage(file="new_btn.gif")
        self.button3 = Button(self.graph_frame, text = 'New day',image=self.igm103,command= self.day_pass)
        self.button3.grid(row = 0,column = 1)
        

##widgets for news_frame
        #sets the two frames - the button frame and picture frame
        self.news_frame_btns.pack_propagate(False)
        self.news_frame.pack_propagate(False)
        #sets the most resent hint
        
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
        quote = ('you have\n'+ str(money))
        v.set(quote)
        r = StringVar()
        Label(self.bank_frame, textvariable=r,bg='#117e34',fg= 'white').pack()
        interest = DB.interest_fetch()
        Main.interest_stats()
        quote = ("Today's interest rate:\n" + str(interest*100) + "%\n\n  Possible money gained \nfrom compound interest:\n"+str(interest_gain)+"")
        r.set(quote)
        
##The menu bar so the user can change Days
        menubar = Menu(window)
        filemenu = Menu(menubar,tearoff=0)
        #add commands to menu
        filemenu.add_command(label="Done?", command = self.done_check)
        filemenu.add_command(label="New Day", command = self.day_pass)
        menubar.add_cascade(label="Day", menu=filemenu)

        #savemenu = Menu(menubar, tearoff=0)
##        #savemenu.add_command(label="Save progress",command = self.pass2save())
        #menubar.add_cascade(label="Save", menu=savemenu)
        window.config(menu=menubar)

##widgets for the stats_frame
        self.stats_frame.grid(sticky=N+S+E+W)
        self.stats_frame.grid_propagate(False)
        
        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#117e34',fg= 'white').grid(row=0,column=0)
        quote = ('Play for Stats')
        v.set(quote)

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
        quote = ('ASSETS:\n\n\nFOOD \n' + str(owned[0]) + '\nHOTELS \n' + str(owned[1]) + '\nTECH \n' + str(owned[2]) +
                 '\nHEALTH \n' + str(owned[3]) + '\nCAR \n' + str(owned[4]) + '\nOIL \n' + str(owned[5]))
        v.set(quote)

##FUNCTION FOR BANK
    def setup_bank(self):
        self.bank_frame.pack_propagate(False)
        v = StringVar()
        Label(self.bank_frame, textvariable=v,bg='#117e34',fg= 'white').pack()
        quote = ('you have\n'+ str(money))
        v.set(quote)
        r = StringVar()
        Label(self.bank_frame, textvariable=r,bg='#117e34',fg= 'white').pack()
        interest = DB.interest_fetch()
        Main.interest_stats()
        quote = ("Today's interest rate:\n" + str(interest*100) + "%\n\n Possible money gained \nfrom compound interest:\n"+str(interest_gain)+"")
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
            
##Creating a new window for the graph
    def new_window(self):
        self.newWindow = Toplevel(window)
        self.app = Graph(self.newWindow)

#Functions for the stats_frame
    def stats_display(self,change_percentage,profit_change):
        #clearing the frame
        list = self.stats_frame.grid_slaves()
        for l in list:
            l.destroy()
        #adding the informtion for each comapany
        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 1, column =1,sticky='NSEW')
        quote = ('FOOD \nPercentage change:  ' + str(change_percentage[0])+'%\nAmount Made:   '+ str(profit_change[0]))
        v.set(quote)

        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 1, column =3,sticky='NSEW')
        quote = ('HOTELS \nPercentage change:  ' + str(change_percentage[1])+'%\nAmount Made:   '+ str(profit_change[1]))
        v.set(quote)

        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 1, column =5,sticky='NSEW')
        quote = ('TECH \nPercentage change:  ' + str(change_percentage[2])+'%\nAmount Made:   '+ str(profit_change[2]))
        v.set(quote)

        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 2, column =1,sticky='NSEW')
        quote = ('HEALTH \nPercentage change:  ' + str(change_percentage[3])+'%\nAmount Made:   '+ str(profit_change[3]))
        v.set(quote)

        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 2, column =3,sticky='NSEW')
        quote = ('CAR \nPercentage change:  ' + str(change_percentage[4])+'%\nAmount Made:   '+ str(profit_change[4]))
        v.set(quote)

        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 2, column =5,sticky='NSEW')
        quote = ('OIL \nPercentage change:  ' + str(change_percentage[5])+'%\nAmount Made:   '+ str(profit_change[5]))
        v.set(quote)

        #adding a divider to make this frame more organised 
        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 3, column =0,columnspan = 7,sticky='NSEW')
        quote = ('-------------------------------------------------------------------------------------------------------------------------')
        v.set(quote)

        #adding a label for each company to display the price of each comapny
        #getting the price of each comany today from the databse 
        todays_prices = DB.today_price()
        
        #creating and positioninf th label for each company
        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 4, column =1,sticky='NSEW')
        quote = ('FOOD Todays Price: '+str(todays_prices[1][0]))
        v.set(quote)

        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row =4, column =3,sticky='NSEW')
        quote = ('HOTELS Todays Price: '+str(todays_prices[2][0]))
        v.set(quote)

        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 4, column =5,sticky='NSEW')
        quote = ('TECH Todays Price: '+str(todays_prices[3][0]))
        v.set(quote)

        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 5, column =1,sticky='NSEW')
        quote = ('HEALTH Todays Price: '+str(todays_prices[4][0]))
        v.set(quote)

        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 5, column =3,sticky='NSEW')
        quote = ('CAR Todays Price: '+str(todays_prices[5][0]))
        v.set(quote)

        v = StringVar()
        Label(self.stats_frame, textvariable=v,bg='#4A6E9B',fg= 'white').grid(row = 5, column =5,sticky='NSEW')
        quote = ('OIL Todays Price: '+str(todays_prices[6][0]))
        v.set(quote)

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
        global interest_gain
        day = day +1
        print(day)

        ## for the stats frame 
        change_percentage = []
        profit_change= []
        
        #Adding profit
        records = DB.price_change()
        for i in range (0,7):
            # working out change for each comapny 
            change = (records[(i*2)+1][0])-(records[i*2][0])

            # working out percentage increades or decreased - as whole number interger
            change_percentage.append(int(round(change/(records[(i*2)+1][0])*100)))

            #stroing the amount of money that comapny has made for the user 
            profit_change.append((change*self.no_owned[i]))
            
            money = money + (change*self.no_owned[i])
            print(money)
        print(profit_change)
        print(change_percentage)
        print(self.no_owned)
        money = money + interest_gain 
        #Refreshing the bank
        Main.interest_stats()
        GUI.clear_bank(self)
        GUI.setup_bank(self)

        #setting up stats frame
        GUI.stats_display(self,change_percentage,profit_change)

##Takes the comapny button pressed in the GUI
##Decrements the number owned list and updates the gui
    def SellAsset(self,company):
        global money
        earned = DB.price(self,company)
        
        print(money)
        print(self.no_owned)
        #check they have stocks in this company
        if self.no_owned[company-1] > 0:
            self.no_owned[company-1] = self.no_owned[company-1] -1
            money = money + earned[0][0]
        #oherwise show error message 
        else:
            tm.showinfo("Own None","You have sold all your stocks")
            
        GUI.ClearAndAssets(self,self.no_owned)

##Takes the comapny button pressed in the GUI
##Increments the number owned list and updates the gui
    def BuyAsset(self,company):
        global money
        earned = DB.price(self,company)
        #check they have enough money
        if (money - earned[0][0]) > 0:
            money = money - earned[0][0]
            self.no_owned[company-1] = self.no_owned[company-1] + 1
        #otherwise show error message
        else:
            tm.showinfo("Bankrupt","You don't have enough money")
            money = money
        print(money)
        
        GUI.ClearAndAssets(self,self.no_owned)

    def interest_stats():
        global interest_gain
        interest = DB.interest_fetch()
        interest_gain = int(round(money * interest))

    def info4save(self):
        global money
        global day
        DB.save(self.no_owned,day,money)
        

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
#useless
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
        print(password + "   " + username)
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
    def graph_points(self):
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
    def price_change():
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        command = ("SELECT price,dayNo,company_ID FROM stock_price WHERE dayNo = '"+ str(day-1) +"'OR dayNo = '"+ str(day) +"'")
        c.execute(command)
        records = c.fetchall()
        return(records)
    
    def today_price():
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        command = ("SELECT price FROM stock_price WHERE dayNo = '"+ str(day) +"'")
        c.execute(command)
        todays_cost = c.fetchall()
        print(todays_cost)
        return(todays_cost)
    
    def interest_fetch():
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        command = ("SELECT price FROM stock_price WHERE dayNo = '"+ str(day) +"'AND company_ID = '7'")
        c.execute(command)
        interest = c.fetchall()
        interest = int(interest[0][0])/100
        print(interest)
        return(interest)
    def save(no_owned,day,money):
        global ID
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        #saving the day
        print(day)
        command = ("UPDATE user_info SET day_of_progress='"+ str(day)+ "' WHERE user_ID='"+str(ID)+"'")
        c.execute(command)
        conn.commit()
        #saving amount of money
        command = ("UPDATE assets SET amount='"+ str(no_owned[6]) + "' WHERE user_ID='"+str(ID)+"'AND company_ID ='7'")
        c.execute(command)
        conn.commit()
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        #saving amount of food
        command = ("UPDATE assets SET amount='"+ str(no_owned[0]) + "' WHERE user_ID='"+str(ID)+"'AND company_ID ='1'")
        c.execute(command)
        conn.commit()
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        #saving amount of hotels
        command = ("UPDATE assets SET amount='"+ str(no_owned[1]) + "' WHERE user_ID='"+str(ID)+"'AND company_ID ='2'")
        c.execute(command)
        conn.commit()
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        #saving amount of tech
        command = ("UPDATE assets SET amount='"+ str(no_owned[2]) + "' WHERE user_ID='"+str(ID)+"'AND company_ID ='3'")
        c.execute(command)
        conn.commit()
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        #saving amount of health
        command = ("UPDATE assets SET amount='"+ str(no_owned[3]) + "' WHERE user_ID='"+str(ID)+"'AND company_ID ='4'")
        c.execute(command)
        conn.commit()
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        #saving amount of car
        command = ("UPDATE assets SET amount='"+ str(no_owned[4]) + "' WHERE user_ID='"+str(ID)+"'AND company_ID ='5'")
        c.execute(command)
        conn.commit()
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        #saving amount of oil
        command = ("UPDATE assets SET amount='"+ str(no_owned[5]) + "' WHERE user_ID='"+str(ID)+"'AND company_ID ='6'")
        c.execute(command)
        conn.commit()
        
        
class Graph():
    def __init__(self, master):
        #getting the 2D array or coordinates from the grpah_points function
        coords = self.graph_points()
        #Linking back to popup window 
        self.master = master
        #creating a frame is display the graph
        self.frame = Frame(master)
        #setting up the graph
        fig = Figure( figsize=(10, 9), dpi=80 )
        ax = fig.add_subplot(111)
        #plotting the lines 
        self.line, = ax.plot(coords[0],label='FOOD')
        self.line, =ax.plot(coords[1],label='HOTELS')
        self.line, =ax.plot(coords[2],label='TECH')
        self.line, =ax.plot(coords[3],label='HEALTH')
        self.line, =ax.plot(coords[4],label='CAR')
        self.line, =ax.plot(coords[5],label='OIL')
        self.line, =ax.plot(coords[6],label='BANK INTEREST')
        #adding a key
        ax.legend()
        #adding a quit button to close the pop up
        self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        #adding the created graph(figure) to a canvas
        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.show()
        #poitioning the graph and quit button in the frame 
        self.quitButton.pack()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #packing the frame into the window
        self.frame.pack()
        

    def graph_points(self):
        global day
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        #2D array to store the graph points
        coords = [[],[],[],[],[],[],[]]
        #loop so databse can be queired for the point of each company one at a time 
        for i in range(0,7):
            command = ("SELECT price FROM stock_price WHERE company_ID = '"+ str(i+1) +"'")
            c.execute(command)
            all_prices = c.fetchall()
            for j in range(0,day+1):
                #setting y coordinates for each comapny
                coords[i].append(all_prices[j])
        return(coords)

    #functionality of the quit button in the graph frame
    def close_windows(self):
        self.master.destroy()
    
                

database = DB()
login= LogIn()
window.mainloop()

