import unittest
import caesar

class TestStringMethods(unittest.TestCase):
    
    def test_rot(self):
        rotation_step = -3
        self.assertEqual(caesar.rot(rotation_step, 'D'), 'A')
        self.assertEqual(caesar.rot(rotation_step, 'C'), 'Z')
