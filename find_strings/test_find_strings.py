#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, find_strings as fs


class TestStringMethods(unittest.TestCase):
    def test_permutate(self):
        self.assertItemsEqual(fs.permutate(''), [['']])
        self.assertItemsEqual(fs.permutate('1'), [['1']])
        self.assertItemsEqual(fs.permutate('12'), [['12'], ['1', '2']])
        self.assertItemsEqual(fs.permutate('123'), [['123'], ['1', '23'], ['12', '3'], ['1', '2', '3']])
        self.assertItemsEqual(fs.permutate('1234'), [['1234'], ['1', '234'], ['1', '2', '34'], ['1', '23', '4'],
                                                     ['12', '34'], ['12', '3', '4'], ['123', '4'],
                                                     ['1', '2', '3', '4']])
        self.assertItemsEqual(fs.permutate('999'), [['999'], ['9', '99'], ['99', '9'], ['9', '9', '9']])

    def test_remove_invalid_permutations(self):
        self.assertItemsEqual(fs.remove_invalid_permutations([]), [])
        self.assertItemsEqual(fs.remove_invalid_permutations([['1']]), [['1']])
        self.assertItemsEqual(fs.remove_invalid_permutations([['12'], ['1', '2']]), [['12'], ['1', '2']])
        self.assertItemsEqual(fs.remove_invalid_permutations([['123'], ['1', '23'], ['12', '3'], ['1', '2', '3']]),
                              [['1', '23'], ['12', '3'], ['1', '2', '3']])
        self.assertItemsEqual(fs.remove_invalid_permutations(
            [['1234'], ['1', '234'], ['1', '2', '34'], ['1', '23', '4'],
             ['12', '34'], ['12', '3', '4'], ['123', '4'], ['1', '2', '3', '4']]),
            [['1', '23', '4'], ['12', '3', '4'], ['1', '2', '3', '4']])

    def test_encode_permutations(self):
        self.assertEqual(fs.encode_permutations([]), [])
        self.assertEqual(fs.encode_permutations([['1']]), [['A']])
        self.assertEqual(fs.encode_permutations([['12']]), [['L']])
        self.assertEqual(fs.encode_permutations([['12'], ['1', '2']]), [['L'], ['A', 'B']])
