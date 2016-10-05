#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
