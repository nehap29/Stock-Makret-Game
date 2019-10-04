#######################
#Stop frames resizing : pack_propagate(False) or grid_propagate(False)


#########################


#Import everything from tkinter module
from tkinter import *

#To initialize Tkinter, we have to create a Tk root widget
#which is a window with a title bar
window = Tk()
window.title('Stock Market')
window.geometry('{}x{}'.format(1000, 1000))
window.wm_iconbitmap('icon.ico')

#Initialising global variables
#Amount the user owns of each company
food = ''
hotels= ''
tech= ''
health= ''
car= ''
oil= ''

#How much money the user has
money = 0

#Difficulty chosen by the user 
level = 0

#What day the user is on
day = 0

#List of all the hints
img = ['0.gif', '1.gif', '2.gif', '3.gif']






#################################################################################


#GUI CLASS


#################################################################################


#so that a GUI object can be made that deals with all the visual side
class GUI:

##Everything see on the GUI
    def __init__(self, window, database):

        #A Frame is a container widget which is placed inside a window,
        #which can have its own border and background
        #it is used to group related widgets together in an application’s layout.
        self.assets_frame = Frame(window,bg='#0a561b',width=200, height=1000, pady=3,highlightthickness=4, highlightbackground="#111")
        self.graph_frame = Frame(window,bg='#e15d03',width=800, height=500, pady=3,highlightthickness=4, highlightbackground="#111")
        self.company_frame = Frame(window,bg='#50871c',width=800, height=200, pady=3,highlightthickness=4, highlightbackground="#111")
        self.bank_frame = Frame(window,bg='#117e34',width=300, height=300, pady=3,highlightthickness=4, highlightbackground="#111")
        self.news_frame = Frame(window,bg='#c52800',width=500, height=250, pady=3,highlightthickness=4, highlightbackground="#111")
        self.news_frame_btns = Frame(window,bg='#c52800',width=500, height=50, pady=3,highlightthickness=4, highlightbackground="#111")

##Initially setting the window into a grid structure
        #Layout of the main frames

        #adding a grid to the window
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        #Positioning the frames within that grid
        self.assets_frame.grid(column = 0,columnspan =2, rowspan = 10)
        self.graph_frame.grid(column =2, row= 0, rowspan = 4, columnspan = 8)
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
        self.igm1 = PhotoImage(file="FOOD.gif")
        Button(self.company_frame, image=self.igm1,height=85, width= 250,command=lambda: self.sell('FOOD')).grid(column = 0, row = 0)
        self.igm2 = PhotoImage(file="HOTELS.gif")
        Button(self.company_frame, image=self.igm2,height=85, width= 250,command=lambda: self.sell('HOTELS')).grid(column = 1, row = 0)
        self.igm3 = PhotoImage(file="TECH.gif")
        Button(self.company_frame, image=self.igm3,height=85, width= 250,command=lambda: self.sell('TECH')).grid(column = 2, row = 0)
        self.igm4 = PhotoImage(file="HEALTH.gif")
        Button(self.company_frame, image=self.igm4,height=85, width= 250,command=lambda: self.sell('HEALTH')).grid(column = 0, row = 1)
        self.igm5 = PhotoImage(file="CAR.gif")
        Button(self.company_frame, image=self.igm5,height=85, width= 250,command=lambda: self.sell('CAR')).grid(column = 1, row = 1)
        self.igm6 = PhotoImage(file="OIL.gif")
        Button(self.company_frame, image=self.igm6,height=85, width= 250,command=lambda: self.sell('OIL')).grid(column = 2, row = 1)

##widgets for assets frame
        #Getting rid of the elasticity of the frame, so it size remains when widgets are added
        #Setting this frame as pack as positioning less important
        self.assets_frame.pack_propagate(False)
        #Adding scroll bar and Textbox widget
        Scroll_assets = Scrollbar(self.assets_frame)
        Textbox = Text(self.assets_frame,)
        #Madething the two widegts fill the frame
        #Putt scroll bar vertically so the user can scroll down
        Scroll_assets.pack(side=RIGHT, fill=Y)
        Textbox.pack(side=LEFT, fill=Y, padx=5, pady=5)
        #Connecting the textbox and the scroll bar
        Scroll_assets.config(command=Textbox.yview)
        Textbox.config(yscrollcommand=Scroll_assets.set)
        #Requests database class to load the users current assets to the associated gloabl variable
        #Self as its passing that instnce of the object 
        DB.show_assets(self)

        #Concatenating a string f all the global variables
        quote = (money,'\n' ,food ,'\n', hotels ,'\n', tech ,'\n' , health ,'\n' , car ,'\n' , oil)
        #Displaying the string in the textbox
        Textbox.insert(END, quote)

##widgets for graph_frame
        #Getting rid of the elasticity of the frame, so it size remains when widgets are added
        #Setting this frame as pack as positioning less important
        self.graph_frame.pack_propagate(False)
        self.graph = Canvas(self.graph_frame, width=600, height=200,)
        self.graph.pack()
        # x values go left to right, y values go top to bottom
        # line drawn from (1,195) to (500,195)
        self.graph.create_line(1, 195, 500, 195, fill="black", width=3)

##widgets for news_frame
        #Getting rid of the elasticity of the frame, so it size remains when widgets are added
        #Setting this frame as pack as positioning less important
        #sets the two frames - the button frame and picture frame
        self.news_frame_btns.pack_propagate(False)
        self.news_frame.pack_propagate(False)
        #sets the first image 
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
            Main.day_change()
        else:
            print('click done first')
            
#Sends the name of the company button in the company_frame to the Main class
    def sell(self,company):
        print(company)
        Main.SellAsset(company)



#Functions for the news_frame
    #initialising the pointer - so that we can index img list full of images
    i = 0
    #clears the picture in the picture frame so only one can be see at a time
    def clear(self):
        list = self.news_frame.pack_slaves()
        for l in list:
            l.destroy()
    #decrements the pointer
    def back_btn(self):
        print(self.i)
        if self.i >= 1:
            self.clear()
            self.i = self.i - 1
            print(self.i)
            self.img_update()
        #so image does not change when they are looking at the first picture
        else:
            self.i = 0
            #self.back.config(state='disabled')
            #self.next.config(state='active')
    #increments pointer
    def next_btn(self):
        self.clear()
        print(self.i)
        if self.i < (len(img) - 1):
            self.i = self.i + 1
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
        self.clear()
        self.i = day
        print(self.i)
        self.igm = PhotoImage(file=img[day])
        pic = Button(self.news_frame, image=self.igm)
        pic.pack(side = BOTTOM)


##Communicates between DB amd GUI classes
##as per the Model View Controller development style
class Main:
##Changed the global variable day for the whole program
    def day_change():
        global day
        day = day +1
        print(day)

##Takes the comapny button pressed in the GUI
##Passes the unique identifier of that comapny to the DB class
    def SellAsset(company):
        global money
        if company == 'FOOD':
            money = money + 1
            print(money)
        else:
            print('hi')

            
##Handels all databse interaction
class DB:
##Initalising an object of the database class
    def __init__(self):
        self.u = 9
##Collects the Assets for the user from the database
    #Sets them to global variables
    def show_assets(self):
        global food
        global hotels
        global oil
        global tech
        global health
        global car
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        c.execute('SELECT amount FROM assets WHERE company_ID = 1')
        food = c.fetchall()
        c.execute('SELECT amount FROM assets WHERE company_ID = 2')
        hotels = c.fetchall()
        c.execute('SELECT amount FROM assets WHERE company_ID = 3')
        tech = c.fetchall()
        c.execute('SELECT amount FROM assets WHERE company_ID = 4')
        health = c.fetchall()
        c.execute('SELECT amount FROM assets WHERE company_ID = 5')
        car = c.fetchall()
        c.execute('SELECT amount FROM assets WHERE company_ID = 6')
        oil = c.fetchall()
        print(oil)

##Collects the users chosen level of difficulty from the databse
    def difficulty():
        global level
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        c.execute('SELECT difficulty FROM assets WHERE user_ID = 1')
        level = c.fetchall()
        
######## graph ###########
#code that will bring up the points that need to be plotted for each comapny day by dy
#    day = 2
#    for i in range(0,day+1):
#
#        for j in range(i,len(data),30):
#            print(data[j][2])
#
#

database = DB()
gui = GUI(window,database)
print(oil)
window.mainloop()









