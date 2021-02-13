class Credential:
    """
    Class thst saves user credentails 
    """

    credentail_list = [] # empty list of credentials 

def __init__(self,account,username,password):
    
     """
    __init__ method helps us define properties for our object
    
     Args:
         account: New credential account.
         username: New credential username.
         password: New credential password.
     
    """
self.account = account
self.username = username 
self.password = password

def add_credential(self):
        """
        method to save a new credential to the credential_list.
        """
        Credential.credential_list.append(self)

def delete_credential(self):
        """
        delete_credential method deletes a saved credential form the credential_list
        """
        Credential.credential_list.remove(self)  