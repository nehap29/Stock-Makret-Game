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


img = ['0.gif', '1.gif', '2.gif', '3.gif']
finishDay = True
day = 0
money = 0


#################################################################################


#GUI CLASS


#################################################################################


#so that a GUI object can be made that deals with all the visual side
class GUI:
    i = 0
    def done_check():
        global finishDay
        finishDay = True
        print('ur done')
        
    def day_pass():
        global finishDay
        if finishDay == True:
            Main.day_change()
        else:
            print('click done first')

    menubar = Menu(window)
    filemenu = Menu(menubar,tearoff=0)

    # add commands to menu
    filemenu.add_command(label="Done?", command = done_check)
    filemenu.add_command(label="New Day", command = day_pass)
    menubar.add_cascade(label="Day", menu=filemenu)
    window.config(menu=menubar)



    
    def __init__(self, window):
         #A Frame is a container widget which is placed inside a window,
        #which can have its own border and background
        #it is used to group related widgets together in an application’s layout.
        assets_frame = Frame(window,bg='#0a561b',width=200, height=1000, pady=3,highlightthickness=4, highlightbackground="#111")
        graph_frame = Frame(window,bg='#e15d03',width=800, height=500, pady=3,highlightthickness=4, highlightbackground="#111")
        company_frame = Frame(window,bg='#50871c',width=800, height=200, pady=3,highlightthickness=4, highlightbackground="#111")
        bank_frame = Frame(window,bg='#117e34',width=300, height=300, pady=3,highlightthickness=4, highlightbackground="#111")
        news_frame = Frame(window,bg='#c52800',width=500, height=250, pady=3,highlightthickness=4, highlightbackground="#111")
        news_frame_btns = Frame(window,bg='#c52800',width=500, height=50, pady=3,highlightthickness=4, highlightbackground="#111")


        #Layout of the main frames
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        assets_frame.grid(column = 0,columnspan =2, rowspan = 10)
        graph_frame.grid(column =2, row= 0, rowspan = 4, columnspan = 8)
        company_frame.grid(column = 2,row = 5,rowspan = 2, columnspan = 8)
        news_frame.grid(column = 2, row =8, rowspan = 2, columnspan = 5)
        news_frame_btns.grid(column = 2,columnspan = 5,row=7)
        bank_frame.grid(column= 7, row = 7 , columnspan = 3 , rowspan = 3)

        #widgets for graph_frame
        graph_frame.pack_propagate(False)
        graph = Canvas(graph_frame, width=600, height=200,)
        graph.pack()
        # x values go left to right, y values go top to bottom
        # line drawn from (1,195) to (500,195)
        graph.create_line(1, 195, 500, 195, fill="black", width=3)

        #widgets for company_frame

        def sell(company):
            print(company)
            Main.SellAsset(company)
            
        company_frame.grid_propagate(False)
        self.igm1 = PhotoImage(file="FOOD.gif")
        Button(company_frame, image=self.igm1,height=85, width= 250,command=lambda: sell('FOOD')).grid(column = 0, row = 0)
        self.igm2 = PhotoImage(file="HOTELS.gif")
        Button(company_frame, image=self.igm2,height=85, width= 250,command=lambda: sell('HOTELS')).grid(column = 1, row = 0)
        self.igm3 = PhotoImage(file="TECH.gif")
        Button(company_frame, image=self.igm3,height=85, width= 250,command=lambda: sell('TECH')).grid(column = 2, row = 0)
        self.igm4 = PhotoImage(file="HEALTH.gif")
        Button(company_frame, image=self.igm4,height=85, width= 250,command=lambda: sell('HEALTH')).grid(column = 0, row = 1)
        self.igm5 = PhotoImage(file="CAR.gif")
        Button(company_frame, image=self.igm5,height=85, width= 250,command=lambda: sell('CAR')).grid(column = 1, row = 1)
        self.igm6 = PhotoImage(file="OIL.gif")
        Button(company_frame, image=self.igm6,height=85, width= 250,command=lambda: sell('OIL')).grid(column = 2, row = 1)

###########################################################

        #widgets for assets_frame
        def ask():
            DB.show_assets()
            
        def info_delivery(no_food,no_hotels,no_tech,no_health,no_car,no_oil):
            print(no_food,no_hotels,no_tech,no_health,no_car,no_oil)
            return(no_food,no_hotels,no_tech,no_health,no_car,no_oil)

        assets_frame.pack_propagate(False)
        Scroll_assets = Scrollbar(assets_frame)
        Textbox = Text(assets_frame,)
        Scroll_assets.pack(side=RIGHT, fill=Y)
        Textbox.pack(side=LEFT, fill=Y, padx=5, pady=5)
        Scroll_assets.config(command=Textbox.yview)
        Textbox.config(yscrollcommand=Scroll_assets.set)
        global money
        money = str(money)
        ask()
        quote = (money  +'\n hi \n test')
        money = int(money)
        Textbox.insert(END, quote)

############################################################

        #widgets for news_frame
        news_frame_btns.pack_propagate(False)
        news_frame.pack_propagate(False)
        self.igm = PhotoImage(file=img[self.i])
        pic = Button(news_frame, image=self.igm)
        pic.pack(side = BOTTOM)

        
        def clear():
            list = news_frame.pack_slaves()
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
            pic = Button(news_frame, image=self.igm)
            pic.pack(side = BOTTOM)
        def present():
            clear()
            global day
            self.i = day
            print(self.i)
            self.igm = PhotoImage(file=img[day])
            pic = Button(news_frame, image=self.igm)
            pic.pack(side = BOTTOM)

        self.back = Button(news_frame_btns,text = 'Back',command = back_btn)
        self.back.pack(side = LEFT)
        self.next = Button(news_frame_btns,text = 'Next',command = next_btn)
        self.next.pack(side = RIGHT)
        self.current = Button(news_frame_btns,text = 'Current',command = present)
        self.current.pack()

class Main:
    def day_change():
        global day
        day = day +1
        print(day)

    def SellAsset(company):
        global money
        if company == 'FOOD':
            money = money + 1
            print(money)
        else:
            print('hi')

class DB:

    def show_assets():
        import sqlite3
        conn = sqlite3.connect('stock.db')
        c = conn.cursor()
        c.execute('SELECT amount FROM assets WHERE company_ID = 1')
        no_food = c.fetchall()
        c.execute('SELECT amount FROM assets WHERE company_ID = 2')
        no_hotels = c.fetchall()
        c.execute('SELECT amount FROM assets WHERE company_ID = 3')
        no_tech = c.fetchall()
        c.execute('SELECT amount FROM assets WHERE company_ID = 4')
        no_health = c.fetchall()
        c.execute('SELECT amount FROM assets WHERE company_ID = 5')
        no_car = c.fetchall()
        c.execute('SELECT amount FROM assets WHERE company_ID = 6')
        no_oil = c.fetchall()
       
######## graph ###########3
#    day = 2
#    for i in range(0,day+1):
#
#        for j in range(i,len(data),30):
#            print(data[j][2])
#
#


gui = GUI(window)
window.mainloop()
#
