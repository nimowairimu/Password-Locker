class User():
    """
    Class for user log in 
    """
    user_list = []# empty list of logged in users 

def __init__(self,name, password):
        """
        method that defines the properties of a user.
        """
        self.name = name
        self.password = password


def add_user(name,password):
    """
    method to add the user into the system
    """
    User.user_list.append(self)


def login(name,password):# login functions to the password locker 
    """
    method to log in user
    """
    print("Please enter your login details")
    name = input("Enter your username: ")
    password = input("Enter your password : ")
    print("Welcome")
    
     
def register():
    """
    method to register a new user 
    """

    print("Enter your name and password ")
    name = input("Enter your username: ")
    password = input("Enter your password : ")
    login()

def enter():

    """
    method to check if a user is a returning user or a new one 
    """

    print ("Stressing about your passwords? Don't worry , Password Locker got you!")
    ask = input("Do you have an accout ? y/n:  ")
    if ask == "y".lower():
        login()

    elif ask == "n".lower():
        register()
    else:
        enter()


enter()

    