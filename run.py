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
    # log in or register a user

enter()
print(f"Hello {user_name}. what would you like to do? \n Use these short codes : sc - create a new credential, dc - delete credential, fc -find a co, ex -exit the contact list ")
print("


   