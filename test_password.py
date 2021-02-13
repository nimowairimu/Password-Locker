import unittest
from credentials import Credential
from user import User

class TestCredential(unittest.TestCase):
    """
    Test class that defines our test cases for the credential class.
    
    Args:
        Unittest.Testcase:Testcase class that helps in creating test cases
    """
    def setUp(self):
         """
        setUp method to run before each test case.
        
         """

    self.new_credential = Credential("Instagram","wairimu","123")# create a new credential pbject

    def test_init(self):

       """
       test_init test case to test if the object is initialized properly
       """

       self.assetEqual(self.new_credential.account,"Instagram")
       self.assetEqual(self.new_credential.username,"wairimu") 
       self.assetEqual(self.new_credential.password,"123")


if __name__=='__main__':
    unittest.main()
