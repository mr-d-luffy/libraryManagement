# inbuilt modules of python
import sqlite3 as sql
from colorama import Fore
from json import load

# loading of api file
try:
    api = load(open("api/data.json"))
except(Exception) as e:
    print(Fore.RED, "File Path Error", Fore.RESET)

# database class with all functions
class database():
    # connection and initization of database
    def __init__(self):
        super().__init__()
        try:
            self.connection = sql.connect(api["path"][2], timeout=5)
            self.c = self.connection.cursor()
        except(Exception) as e :
            print(Fore.RED, e, Fore.RESET)

    # Database closing function
    def close_connection(self):
        """THIS FUNCTION CLOSE DATBASE CONNECTION"""
        if self.connection:
            self.connection.close()
            print(Fore.GREEN, "Connection closed", Fore.WHITE)

    # Create user in database 
    def createUser(self, userName, userID, contact, city, pincode):
        self.c.execute(f"CREATE TABLE IF NOT EXISTS usersX (name text, id text, contact text, city text, pincode text)")
        self.c.execute(f"INSERT INTO usersX VALUES (?, ?, ?, ?)", (userName, userID, contact, city, pincode))
        self.connection.commit()
        # self.connection.close()

    # Delete user from database
    def deleteUser(self, userID):
        self.c.execute(f"DROP TABLE {userID}")
        self.c.execute(f"DELETE * FROM usersX WHERE id = {userID}")
        self.connection.commit()
        # self.connection.close()
    
    # add new book to database
    def addBook(self, bookName, bookID, dateTime):
        self.c.execute(f"CREATE TABLE IF NOT EXISTS booksX (bookName text, bookID text, dateTime text)")
        self.c.execute(f"INSERT INTO booksX VALUES (?, ?, ?)", (bookName, bookID, dateTime))
        self.connection.commit()
        # self.connection.close()

    # Delete outdated books from database
    def deleteBook(self, bookID):
        self.c.execute(f"DELETE * FROM booksX WHERE bookID = {bookID}")
        self.connection.commit()
        # self.connection.close()
    
    # This function work for issue book to user
    def borrowBook(self, userID, bookName, bookID, dateTime):
        self.c.execute(f"CREATE TABLE IF NOT EXISTS {userID} (bookName text, bookID text, dateTime text)")
        self.c.execute(f"INSERT INTO {userID} VALUES (?, ?, ?)", (bookName, bookID, dateTime))
        self.connection.commit()
        # self.connection.close()

    # This function work for unissue book from user
    def unborrowBook(self, userID, bookName, bookID):
        self.c.execute(f"DELETE * FROM {userID} WHERE bookID = {bookID} OR bookName = {bookName}")
        self.connection.commit()
        # self.connection.close()

    # check login status from database
    def adminLoginCheck(self, userName, userPassword):
        self.c.execute("SELECT * FROM adminX")
        self.data = self.c.fetchall()
        
        if self.data[0][0] == userName:
            if self.data[0][1] == userPassword:
                self.connection.commit()
                return True
            else:
                return False
        else:
            return False

# testing of functions
if __name__=="__main__":
    db = database()
    # print(db.adminLoginCheck("admin", "admin@123"))
    db.createUser("aashu", "Aashu2006", "8788009988", "nagpur", "440024")
