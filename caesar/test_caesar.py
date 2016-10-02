import unittest
import caesar

class TestStringMethods(unittest.TestCase):
    
    def test_rot(self):
        self.assertEqual(caesar.rot('D'), 'A')
        self.assertEqual(caesar.rot('C'), 'Z')
