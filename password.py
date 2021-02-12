
def login():
    print("Please enter your login details")
    name = input("Enter your username: ")
    password = input("Enter your password : ")
    print("Welcome")
    
     
def register():
    print("Enter your name and password ")
    name = input("Enter your username: ")
    password = input("Enter your password : ")
    login()

def enter():
    print ("Stressing about your passwords? Don't worry , Password Locker got you!")
    ask = input("Do you have an accout ? y/n:  ")
    if ask == "y".lower():
        login()

    elif ask == "n".lower():
        register()
    else:
        enter()


enter()