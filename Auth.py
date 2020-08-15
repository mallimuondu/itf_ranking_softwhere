from Authlogin import *
import time
def login():
    for i in range(3):
        username = input("pls enter your username: ")
        if username == ' ':
            print("you did n't write any thing")
        else:
            password = input("pls enter pass: ")
            
            with sqlite3.connect('main.db') as db:
                cursour = db.cursor()
            find_user = ('SELECT * FROM login WHERE username = ? AND password = ?')
            cursour.execute(find_user,[(username), (password)])
            results = cursour.fetchall()
            if results:
                for bla in results:
                    malli = str(bla)
                    print("Welcome ")
                break
            elif password == ' ':
                print("you did n't write any thing")
            else:
                print("Username and passwored not recognised")
                again = input("Do u want to try again?(y/n): ")
                if again.lower() == "n":
                    print("Good Bye")
                    time.sleep(1)
                    break
login()