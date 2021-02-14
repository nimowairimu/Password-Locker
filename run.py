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
    return Contact.find_by_number(number)


