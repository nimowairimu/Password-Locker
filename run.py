#!/usr/bin/env python3.6
from credentials import Credential

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

