#######################
#Stop frames resizing : pack_propagate(False) or grid_propagate(False)


###########
##############


#Import everything from tkinter module
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
import hashlib
#import matplotlib
#matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure


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
        #tells the function that other functions can inherit the variables and methods from this function
        #this means i can send what ever the user inputs into the input box to other functions for validation
        super().__init__()

        #assigning a label and an input box for the username
        self.user_label = Label(self, text="Username")
        self.user_entry = Entry(self)
        #positioning the label and input box within the window
        self.user_label.grid(row=0, sticky=E)
        self.user_entry.grid(row=0, column=1)


        #Assigning and positioning the login button
        self.logbtn = Button(self, text="Login", command = self.login_check)
        self.logbtn.grid(row = 5,columnspan=2)

        #assigning a label and an input box for the password
        self.pass_label = Label(self, text="Password")
        #specifying the users input should show in the textbox as *
        self.pass_entry = Entry(self, show="*")
        #positioning the label and input box within the window
        self.pass_label.grid(row=3, sticky=E)
        self.pass_entry.grid(row=3, column=1)

        self.grid()

    #validating the username
    def login_check(self):
        #inheriting the username input from the __init__ function
        username = self.user_entry.get()
        #calling database class to check if this username exists in the DB
        found = DB.userexist(self,username)
        print(found)
        #if found in the database calls the password validation method
        if found == True:
            LogIn.pass_enter(self,username)
        #else program is sent back to the start where user can try to log in again
        else:
            LogIn()
    #validating the password  
    def pass_enter(self,username):
        #inheriting the password input from the __init__ function
        password = self.pass_entry.get()
        print('password entered:' , password)
        #calling database class to check if this password corresponds with the username in the DB
        foundpass = DB.passexist(self,password,username)
        print(foundpass)
        #if password is also correct
        if foundpass == True:
            #pop up to show sucessful log in
            tm.showinfo("Login", "Hiya Neha")
            #GUI window initalised 
            window.title('Stock Market')
            window.geometry('{}x{}'.format(1000, 1000))
            window.wm_iconbitmap('ICON.ico')
            #Dataabse class called to get all the gloabls of the user that has just logged in
            DB.set_global(self,username)
            #GUI class called and main program is run
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
        self.assets_frame = Frame(window,bg='#0a561b',width=200, height=1000, pady=3,highlightthickness=4, highlightbackground="#111")
        self.graph_frame = Frame(window,bg='#e15d03',width=800, height=500, pady=3,highlightthickness=4, highlightbackground="#111")
        self.company_frame = Frame(window,bg='#50871c',width=800, height=200, pady=5,padx =7,highlightthickness=4, highlightbackground="#111")
        self.bank_frame = Frame(window,bg='#117e34',width=300, height=300, pady=3,highlightthickness=4, highlightbackground="#111")
        self.news_frame = Frame(window,bg='#c52800',width=500, height=250, pady=3,highlightthickness=4, highlightbackground="#111")
        self.news_frame_btns = Frame(window,bg='#c52800',width=500, height=50, pady=3,highlightthickness=4, highlightbackground="#111")

##Initially setting the window into a grid structure
        #Layout of the main frames

        #adding a grid to the window
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        #Positioning the frames within that grid
        self.assets_frame.grid(column = 0,columnspan =2,row=2,rowspan = 10)
        self.graph_frame.grid(column =2, row= 0, rowspan = 4,  columnspan = 8)
        self.company_frame.grid(column = 2,row = 5,rowspan = 2, columnspan = 8)
        self.news_frame.grid(column = 2, row =8, rowspan = 2, columnspan = 5)
        self.news_frame_btns.grid(column = 2,columnspan = 5,row=7)
        self.bank_frame.grid(column= 7, row = 7 , columnspan = 3 , rowspan = 3)
        
##widgets for company_frame
        #Getting rid of the elasticity of the frame, so it size remains when widgets are added
        #Also setting this frame up as a grid
        self.company_frame.grid_propagate(False)
        #Setting the image to a variable that can be refrenced
        #Creating a button (In company frame, with this image, button of this size,when pressed call DB).(put in grid ar this position)
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
        #Getting rid of the elasticity of the frame, so it size remains when widgets are added
        #Setting this frame as pack as positioning less important
        self.assets_frame.pack_propagate(False)
        #setting up string variable that can be displayed in a label
        v = StringVar()
        #creating a label with a chosen background colour and white text 
        Label(self.assets_frame, textvariable=v,bg='#0a561b',fg= 'white').pack()
        #Requests database class to load the users current assets
        numbers = Main.info4assets(self)
        print(numbers)
        #Concatenating a string of all the values in the returned assets list
        quote = ('FOOD \n' + str(numbers[0]) + '\nHOTELS \n' + str(numbers[1]) + '\nTECH \n' + str(numbers[2]) +
                 '\nHEALTH \n' + str(numbers[3]) + '\nCAR \n' + str(numbers[4]) + '\nOIL \n' + str(numbers[5]))
        v.set(quote)

##widgets for graph_frame
        #getting points from the databse class
        coords = DB.graph_points(self)
        #importing matplotlib library so graph can be drawn
        import matplotlib.pyplot as plt
        #Indeexing all the coords for each company from the 2D array returned by the DB
        plt.plot(coords[0],label='comp1')
        plt.plot(coords[1],label='comp2')
        plt.plot(coords[2],label='comp3')
        plt.plot(coords[3],label='comp4')
        plt.plot(coords[4],label='comp5')
        plt.plot(coords[5],label='comp6')
        plt.plot(coords[6],label='comp7')

        #specifying name of graph and laels for the axis
        plt.title('STOCK MARKET')
        plt.ylabel('price')
        plt.xlabel('day')
        #adding a key so the user knows which line represents which company 
        plt.legend()
        
        plt.show()
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
        #adding a labels to the bank frame to display the amount of money the user has
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
        #Putting the Done? and New Day into a drop down menu
        menubar.add_cascade(label="Day", menu=filemenu)
        window.config(menu=menubar)

##functions for changing the day - functionallity for the menu buttons
    #checks user is done with the current day
    def done_check(self):
        self.finishDay = True
        print('ur done')
    #changes the day
    def day_pass(self):
        if self.finishDay == True:
            #chaing day is a responsibility of the main class so the main class is called
            Main.day_change()
        else:
            print('click done first')
#buying and selling fucntions           
#Sends the name of the company button in the company_frame to the Main class
#Calls functions to update money in the bank 
    def sell(self,company):
        #clears the bank ready to display updated money variable
        self.clear_bank()
        #Calls main to perform all the changing variable functionality
        Main.SellAsset(self,company)
        #calls function to remake the bank using the new value for money 
        self.setup_bank()
    def buy(self,company):
        #clears the bank ready to display updated money variable
        self.clear_bank()
        #Calls main to perform all the changing variable functionality
        Main.BuyAsset(self,company)
        #calls function to remake the bank using the new value for money 
        self.setup_bank()

#function to update the assets frame by clearing it and remaking it with the new variables     
    def ClearAndAssets(self,owned):
        #clearing the assets frame 
        list = self.assets_frame.pack_slaves()
        for l in list:
            l.destroy()
        #remaking the assets frame - same code as in the constructor function in the GUI class
        v = StringVar()
        Label(self.assets_frame, textvariable=v,bg='#0a561b',fg= 'white').pack()
        #Requests database class to load the users current assets
        quote = ('FOOD \n' + str(owned[0]) + '\nHOTELS \n' + str(owned[1]) + '\nTECH \n' + str(owned[2]) +
                 '\nHEALTH \n' + str(owned[3]) + '\nCAR \n' + str(owned[4]) + '\nOIL \n' + str(owned[5]))
        v.set(quote)
        
##FUNCTION FOR BANK
    def setup_bank(self):
        # this function is used to remake the bank frame
        #after it has been cleared adn the relevant variablles have been updated
        #it is the same code as in the constuctor method of the GUI class
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
        #this function is used to clear the bank so it can be refreshed to diplay the updated variables
        list = self.bank_frame.pack_slaves()
        for l in list:
            l.destroy()

            
##Functions for the news_frame
    #clears news frame after user clicks navigation buttons
    #so that new image can be displayed
    def clear_news(self):
        list = self.news_frame.pack_slaves()
        for l in list:
            l.destroy()
        
    #functionality for the news frame back button
    def back_btn(self):
        print(self.i)
        if self.i >= 1:
            #clears news frame ready to be refreshed
            self.clear_news()
            #reduces the pointer by the level the user is at
            self.i = self.i - level
            print(self.i)
            #remaking the news frame to show the image the pointer has moved to
            self.img_update()
        #so image does not change when they are looking at the first picture
        else:
            self.i = 0
            #self.back.config(state='disabled')
            #self.next.config(state='active')
    #increments pointer
    def next_btn(self):
        #clears news frame ready to be refreshed
        self.clear_news()
        print(self.i)
        #working out the next hint the user is supposed to see
        #base on their day of progress and level of difficulty
        if self.i < (day*level) and (self.i + level)<=(len(img)-1) and (day%level == 0):
            self.i = self.i + level
            print(self.i)
        #remaking the news frame to show the image the pointer has moved to           
        self.img_update()
        #else:
            #self.next.config(state='disabled')
            #self.back.config(state='active')
        
    #updates the displayed image when called by button functions back and next and present
    def img_update(self):
        self.igm = PhotoImage(file=img[self.i])
        pic = Button(self.news_frame, image=self.igm)
        pic.pack(side = BOTTOM)
        
    #moves the pointer so that the image displayed is the most resent hint the user recieved
    def present(self):
        #clears news frame ready to be refreshed
        self.clear_news()
        print(self.i)
        #works out the more recent hint the user is supposed to see 
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
    
##Changed the global variable day for the whole program
    def day_change():
        global day
        day = day +1
        print(day)
        
#initially gets the number owned assets from the database
    def info4assets(self):
        numbers = DB.show_assets(self)
        print(numbers)
        #returns the information in a 2D array
        #asignment of the array we are going to wirte the needed values to
        self.no_owned = []
        #stripping the 2D array from the DB and writing the relvant values to no_owned array
        for i in range (0,len(numbers)):
            self.no_owned.append(numbers[i][2])
        return(self.no_owned)


##Takes the comapny button pressed in the GUI
##Decrements the number owned list and updates the gui
    def SellAsset(self,company):
        global money
        earned = DB.price(self,company)
        money = money + earned[0][0]
        print(money)
        self.no_owned[company-1] = self.no_owned[company-1] -1
        print(self.no_owned)
        GUI.ClearAndAssets(self,self.no_owned)

##Takes the comapny button pressed in the GUI
##Increments the number owned list and updates the gui
    def BuyAsset(self,company):
        global money
        earned = DB.price(self,company)
        money = money - earned[0][0]
        print(money)
        self.no_owned[company-1] = self.no_owned[company-1] + 1
        print(self.no_owned)
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
#setting all the global variables once the user has logged in 
    def set_global(self,username):
        global ID
        global day
        global level
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        #getting all the username from the user table to find which record raltes to this user
        command = ('SELECT username FROM user_info')
        c.execute(command)
        user_list = c.fetchall()
        #looping through the username to find the correct record
        for i in range (0,len(user_list)):
            #if record found:
            if (user_list[i][0]) == username:
                #all of that record it returned from the dataabse and the relevant values are assigned to the correct global variables
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
        #currently only the assets of user 1 has been written to the dataabse
        #in the future the global variable ID will be used and any user's assets can be retrieved
        ID = '1'
        command = ("SELECT * FROM assets WHERE user_ID ='"+ ID +"'")
        c.execute(command)
        got_numbers = c.fetchall()
        money = got_numbers[6][2]
        return(got_numbers)


##Collects the users chosen level of difficulty from the databse
##useless
#    def difficulty():
#        global level
#        import sqlite3
#        conn = sqlite3.connect('stock.db')
#        c = conn.cursor()
#        c.execute('SELECT difficulty FROM assets WHERE user_ID = 1')
#        level = c.fetchall()

##Collects the Assets for the user from the database 
    def price(self,company):
        global day
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        command = ('SELECT price FROM stock_price WHERE company_ID = ' + str(company) + ' AND dayNo ='+ str(day))
        c.execute(command)
        return(c.fetchall())

#Checks if the username inputted in the login window exists as a record in the datasbe 
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

#checks if the password enetered matches the record of the username
#returns true or false
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
    def graph_points(self):
        global day
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        #2D array so i can store points in an organised system so they will be easy to refrence and plot using matplitlib
        coords = [[],[],[],[],[],[],[]]
        #a loop so for each company the prices can be retieved and written to the 2d array
        #i is the company_ID
        for i in range(0,7):
            #have to do i+1 win the SQL command due to issues with the first record of the datasbe 
            command = ("SELECT price FROM stock_price WHERE company_ID = '"+ str(i+1) +"'")
            c.execute(command)
            all_prices = c.fetchall()
            #a loop to get the prices for that comapny from the returned 3D array
            #and append the prices in day order to the 2D array in the correct index
            # the index of each inner list relates to the compnay_id for that company 
            for j in range(0,day+1):
                #setting y coordinates for each comapny
                coords[i].append(all_prices[j])
        #returning 2D array of cordinates so they can be plotted 
        return(coords)
        
                
                
#making an instance of the databse class so the functions can be used
database = DB()
#making an instance of the login class
#which will automatically call the GUI and Main Class when it is done running
login= LogIn()

window.mainloop()

