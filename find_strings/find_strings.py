#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def permutate(string):
    """ Generate all possible permutations of given string in given order
    :param string: string to generate permutations
    :return: a list of all permutations
    """
    result = [[string]]
    for i in range(1, len(string)):
        first = [string[:i]]
        rest = string[i:]
        for p in permutate(rest):
            result.append(first + p)
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
        for permutation in permutate(number):
            print(permutation)