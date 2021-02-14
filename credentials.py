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