#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, find_strings as fs


class TestStringMethods(unittest.TestCase):
    def test_permutate(self):
        maxInt = 26
        self.assertItemsEqual(fs.permutate('', maxInt), [])
        self.assertItemsEqual(fs.permutate('1', maxInt), [['1']])
        self.assertItemsEqual(fs.permutate('12', maxInt), [['12'], ['1', '2']])
        self.assertItemsEqual(fs.permutate('123', maxInt), [['1', '23'], ['12', '3'], ['1', '2', '3']])
        self.assertItemsEqual(fs.permutate('1234', maxInt), [['1', '23', '4'], ['12', '3', '4'], ['1', '2', '3', '4']])
        self.assertItemsEqual(fs.permutate('999', maxInt), [['9', '9', '9']])

    def test_encode_permutations(self):
        self.assertEqual(fs.encode_permutations([]), [])
        self.assertEqual(fs.encode_permutations([['1']]), [['A']])
        self.assertEqual(fs.encode_permutations([['12']]), [['L']])
        self.assertEqual(fs.encode_permutations([['12'], ['1', '2']]), [['L'], ['A', 'B']])
