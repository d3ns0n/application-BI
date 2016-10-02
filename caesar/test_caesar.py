#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import caesar

class TestStringMethods(unittest.TestCase):
    
    def test_rot(self):
        rotation_step = -3
        self.assertEqual(caesar.rot(rotation_step, 'D'), 'A')
        self.assertEqual(caesar.rot(rotation_step, 'C'), 'Z')
        self.assertEqual(caesar.rot(rotation_step, '!'), '!')
        self.assertEqual(caesar.rot(rotation_step, ','), ',')
        
    def test_encrypt(self):
        self.assertEqual(caesar.encrypt('HELLO'), 'EBIIL')
        self.assertEqual(caesar.encrypt('1!.;$&ä'), '1!.;$&ä')
        self.assertEqual(caesar.encrypt('HELLO.'), 'EBIIL.')
        
    def test_decrypt(self):
        self.assertEqual(caesar.decrypt('EBIIL'), 'HELLO')
        self.assertEqual(caesar.decrypt('1!.;$&ä'), '1!.;$&ä')
        self.assertEqual(caesar.decrypt('EBIIL.'), 'HELLO.')
