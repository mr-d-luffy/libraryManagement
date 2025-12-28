# modules for create app 
from tkinter import *
from json import load
from colorama import Fore
# private modules
from modules.system import system
from modules.database import database
from modules.library import library

# loading of api file
try:
    api = load(open("api/data.json"))
except(Exception) as e:
    print(Fore.RED, "File Path Error", Fore.RESET)

# main window ui class
# connections of all modules
class main(Tk, system, database):
    def __init__(self):
        Tk.__init__(self)
        system.__init__(self)
        database.__init__(self)
        library.__init__(self)

    # main ui of app 
    def App(self):
        #customer Name input
        Label(text="Customer Name : ", fg=api["fontColor"], bg=api["background"]).place(x=10, y=15)
        E1 = Entry(fg=api["fontColor"], bg=api["background"])
        E1.place(x=130, y=13)

        # customer id input
        Label(text="Customer Id : ", fg=api["fontColor"], bg=api["background"]).place(x=330, y=15)
        E2 = Entry(fg=api["fontColor"], bg=api["background"])
        E2.place(x=430, y=13)
        
        # customer phone input
        Label(text="Customer Phone : ", fg=api["fontColor"], bg=api["background"]).place(x=630, y=15)
        E3 = Entry(fg=api["fontColor"], bg=api["background"])
        E3.place(x=760, y=13)

        # customer city input list
        Label(text="City : ", fg=api["fontColor"], bg=api["background"]).place(x=10, y=50)
        self.selectMenu = StringVar()
        self.selectMenu.set("Choose City")
        self.e4 = OptionMenu(self, self.selectMenu, *api["city"])
        self.e4.place(y=50, x=80)

        # customer pincode input
        Label(text="Customer Pincode : ", fg=api["fontColor"], bg=api["background"]).place(x=210, y=50)
        E3 = Entry(fg=api["fontColor"], bg=api["background"])
        E3.place(x=340, y=50)

        #date on ui 
        Label(text="Date : "+system.currentDate(),fg=api["fontColor"], bg=api["background"]).place(x=10,y=170)

        # Buttons for add book to user account
        bt1 = Button(text="Add Book", fg="black", bg="white", command=self.addBookWindow)
        bt1.place(x=100, y=200)

    # add book to user account using this function 
    def addBookWindow(self):
        app = main()
        Label(app, text="Book Name : ", bg=api["background"], fg=api["fontColor"]).place(x=10, y=10)
        #text field
        self.e1 = Entry(app, bg=api["background"], fg=api["fontColor"], insertbackground="white")
        self.e1.place(x=100, y=10)
        #button
        bt1 = Button(app, text="Submit", fg="black", bg="white", command=self.sbt)
        bt1.place(x=100, y=80)

        app.title(api["AppName"])
        app.geometry("300x250")
        app.configure(bg=api["background"])
        app.resizable(api["window"][0], api["window"][0])
        app.mainloop()

    # this function connected with the addBookWindow Function's button
    # created for submit the data to database
    def sbt(self):
        try:
            bookName = self.e1.get()
            bookID = library.createID()
            dt = system.currentDate()
            database.addBook(self, bookName, bookID, dt)
        except(Exception) as e:
            print(Fore.RED, e, Fore.RESET)

# Admin login window class
class AdminLoginWindow(main): 
    # create ui for admin using this function
    def LoginWindow(self):
        l1 = Label(text="userName : ", bg="black", fg="lime")
        l1.place(y=20, x=5)

        self.e1 = Entry(bg="black", fg="lime", insertbackground="white")
        self.e1.place(y=18, x=80)

        l2 = Label(text="password : ", bg="black", fg="lime")
        l2.place(y=70, x=5)

        self.e2 = Entry(bg="black", fg="lime", insertbackground="white", show="*")
        self.e2.place(y=68, x=80)

        b1 = Button(text="Login", bg="white", fg="black", command=self.checkLogin)
        b1.place(y=140, x=100)

    #check admin login data
    def checkLogin(self):
        self.playsound(api["path"][3])
        userName = self.e1.get()
        password = self.e2.get()
        status = self.adminLoginCheck(userName, password)

        if(status == True):
            print("login into admin window")
            self.mainWindow()
        else:
            print("you are not a admin")
            self.playsound(api["path"][4])

    # main System Window UI
    def mainWindow(self):
        self.destroy()
        app = main()
        app.App()
        app.title(api["AppName"])
        app.resizable(api["window"][0], api["window"][0])
        app.configure(bg=api["background"])
        app.geometry("1000x600")
        app.mainloop()

# execute app from here
# this code also runes at this file only
if __name__=="__main__":
    app = AdminLoginWindow()
    app.LoginWindow()
    app.title(api["AppName"])
    app.resizable(api["window"][0], api["window"][0])
    app.configure(bg=api["background"])
    app.geometry("300x250")
    
    # set icon for App
    try:
        icon = PhotoImage(file=api["path"][5])
        app.iconphoto(False, icon)
    except(Exception) as e:
        print(Fore.RED, e, Fore.RESET)

    app.mainloop()

