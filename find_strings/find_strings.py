#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import ascii_uppercase as uc
import sys


def permutate(string, maxInt):
    """ Generate all possible permutations of given string in given order
    :param string: string to generate permutations
    :return: a list of all permutations
    """
    result = []
    if string and int(string) <= maxInt:
        result.append([string])
    for i in range(1, len(string)):
        first = [string[:i]]
        rest = string[i:]
        for p in permutate(rest, maxInt):
            if int(first[0]) <= maxInt:
                result.append(first + p)
    return result


def encode_permutations(permutations):
    """ Encodes permutations in characters
    :param permutations: a list of permutations
    :return: a list with encoded permutations"""
    result = []
    for permutation in permutations:
        result_element = []
        for element in permutation:
            result_element.append(uc[int(element) - 1])
        result.append(result_element)
    return result


def print_usage():
    print('Usage: find_strings.py <number> \n')
    print('Number: an integer to encode as character \n')
    print('Example: find_strings.py 123')


if __name__ == '__main__':
    if len(sys.argv) != 2:  # if less than 2 arguments given on command line
        print_usage()
    else:
        number = sys.argv[1]
        permutations = permutate(number, len(uc))
        encoded_permutations = encode_permutations(permutations)
        for permutation in encoded_permutations:
            print(permutation)
