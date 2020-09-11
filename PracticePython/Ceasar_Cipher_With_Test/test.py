import unittest
from ceasar import ceasar




class TestCesar(unittest.TestCase):

    def test_coding(self):
        #to check the code working properly, we need to use self.assertEqual method
        self.assertEqual(ceasar('baca',3),'edfd')
    def test_encrypting(self):
        self.assertEqual(ceasar('edfd',-3),'baca')