# -*- coding: utf-8 -*-

# the program counts nxm table permutations such that each element is in the same row or column

import itertools


def check_permutation(permutation, shape):
    # checks if a permutation is valid
    (rows, columns) = shape
    for cell in range(rows*columns):
        flag = 0
        for column in range(columns):
            if (cell == permutation[cell % rows + column * rows]):
                flag = 1
        for row in range(rows):
            if (cell == permutation[(cell // rows) * rows + row]):
                flag = 1
        if flag == 0:
            return False
    return True


def count_all_permutations(shape):
    # count all valid permutations with given shape
    (rows, columns) = shape
    permutations = itertools.permutations(range(rows * columns), rows * columns)
    counter = 0
    for permutation in permutations:
        if (check_permutation(permutation, shape) == True):
            counter += 1
    return counter


shape = (3, 3)  # replace with other matrix shape, if you wish
print(count_all_permutations(shape))
