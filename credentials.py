class Credential:
    """
    Class thst saves user credentails 
    """

    credentail_list = [] # empty list of credentials 

def __init__(self,account,username,password):

    
     """
    __init__ method helps us define properties for our object
     
    """
self.account = account
self.username = username
self.password = password

def save_credential(self):
        """
        method to save a new credential to the credential_list.
        """
        Credential.credential_list.append(self)

def delete_credential(self):
    """
    method to delete a saved credential from the list.
    """
    Credential.credential_list.remove(self)

@classmethod
def find_credential(cls,account):
    '''
     Method that takes in an account and returns the credentials  that matches that account.

     Args:
        Takes the account to search for 
    Returns :
        The credentials that match that account
        '''

    for credential in cls.credential_list:
        if credential.account == account:
            return credential

    @classmethod
    def credential_exist(cls,account):

        '''
        Method that checks if a credential exists from the list.
        Args:
             to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credential in cls.credential_list:
             if credential.account == account:
                    return True

    return False 