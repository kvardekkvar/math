# -*- coding: utf-8 -*-

# the program counts nxm table permutations such that each element is in the same row or column

import itertools


def check_permutation(perm, shape):
    # checks if a permutation is valid
    (n, m) = shape
    for i in range(n*m):
        flag = 0
        for jn in range(m):
            if (i == perm[i % n + jn*n]):  # column
                flag = 1
        for jm in range(n):
            if (i == perm[(i//n)*n + jm]):  # row
                flag = 1
        if flag == 0:
            return False
    return True


def count_all_permutations(shape):
    # count all valid permutations with given shape
    (n, m) = shape
    perm = itertools.permutations(range(n*m), n*m)
    cnt = 0
    for i in perm:
        if (check_permutation(i, shape) == True):
            cnt += 1
    return cnt


shape = (3, 3)  # replace with other matrix shape, if you wish
print(count_all_permutations(shape))
