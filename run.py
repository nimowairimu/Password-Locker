#!/usr/bin/env python3.6
from credentials import Credential
from user import User 


def add_user(name,password):
    """
    Function that adds a user to the password locker
    """
    user.add_user()


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

    
def create_credential(account,username,password):
    """
    Function that creates new credentials 
    """
    new_credential = Credential(account,username,password)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(account):
    '''
    Function that finds a credential by its account  and returns the credential
    '''
    return Credential.find_credential(account)

def check_existing_credentials (account):
    '''
    Function that check if a credential exists with that specific account and return a Boolean
    '''
    return Credential.credential_exist(account)

def display_credential():
    '''
    Function that returns all the saved credentials 
    '''
    return Credential.display_credential()

def copy_credential(account):
    """
    A funct that copies the password using the pyperclip framework
    """
    return Credential.copy_credential(account)

def password_generate():
    '''
    generates a random password for the user.
    '''
    random_password=Credential.password_generate()
    return random_password

def main():
    enter() # log in or register a user
print(f"Hello {user_name}. what would you like to do? \n Use these short codes : ac - create a new credential, dc - delete credential, fc -find a credential, ex -check existing credential")
action = input().lower
if action == 'ac':
    print= ("What account is the credential for:   ")
    account = input().lower 
    while True:
        print = ("EP to enter your own password or GP to generate one: ")
        password_option = input().lower
        if password_option == 'ep':
            password = input("Enter the password:  ")
            save_credential()

        elif password_option == 'gp':
            password = password_generate()
            save_credential()
        else:
            print("Invalid, please try again")

elif action == 'dc':
    print = ("Are you sure you want to delete saved credentials? y/n  ")
    choice  = input().lower
    if choice == 'y':
        print = ("What s the account of the credential you wish to delete?")
        account = input ().lower 
        find_account = find_credential(account)
        delete = find_account.delete_credential()
        print = ("Credential successfully deleted")
    else:
        enter()
elif action == 'fc':
    account  = input("What is the account of the credentials you wish to retrieve  ")
    credential = find_credential(account)
    print = ("Your credentials are {{account}} username : {{username}} password: {{password}}")
    while True:
        print = ("Would you like to copy your credentials to clipboard ?y/n")
        copy = input().lower
        if copy == 'y':
            credential.copy_credential()
        else:
            print("Go back to main menu to choose an option")
elif action == 'ex':
    print = ("Check whether your account credentials exist")
    account = input ("Enter the account you wish to check   ")
    credential_exist(account)
    while True:
        print = ("Your account exists on account : {{account}} username :{{username}} and password :{{password}}")
    else :
        print = ("That account detail does not exist")
        print = ("Add as a new credential")
        save_credential()
else:
    ("Please enter a valid option to continue ")

if __name__ == '__main__':

    main()




   





   