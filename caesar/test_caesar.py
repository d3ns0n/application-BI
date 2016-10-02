import unittest
import caesar

class TestStringMethods(unittest.TestCase):
    
    def test_rot(self):
        rotation_step = -3
        self.assertEqual(caesar.rot(rotation_step, 'D'), 'A')
        self.assertEqual(caesar.rot(rotation_step, 'C'), 'Z')
        
    def test_encrypt(self):
        self.assertEqual(caesar.encrypt('HELLO'), 'EBIIL')
        
    def test_decrypt(self):
        self.assertEqual(caesar.decrypt('EBIIL'), 'HELLO')
