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


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []



    self.new_credential = Credential("Instagram","wairimu","123")# create a new credential pbject

    def test_init(self):

       """
       test_init test case to test if the object is initialized properly
       """

       self.assetEqual(self.new_credential.account,"Instagram")
       self.assetEqual(self.new_credential.username,"wairimu") 
       self.assetEqual(self.new_credential.password,"123")


    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

    def test_delete_credential(self):
            '''
            test_delete_contact to test if we can remove a credential from our  list
            '''
            self.new_credential.save_contact()
            test_credential = Credential("Instagram","wairimu","123") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential(self):
        """
        test to check if the credentials can be found by its account
        """
        self.new_credential.save_credential()
        test_credential = Credential("Yahoo","wangechimungai","kadesho") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_credential("Yahoo")

   
        self.assertEqual(found_credential.account,test_credential.account)
   
    def test_credential_exist(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Twitter","waks ","topple34") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Twitter")

        self.assertTrue(credential_exists)
    