class Credential:
    """
    Class thst saves user credentails 
    """

    credentail_list = []

 def __init__(self,accout,username,password):

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