# -*- coding: utf-8 -*-

# the program counts nxm table permutations such that each element is in the same row or column

import itertools


from itertools import combinations, chain
import numpy as np


def binary_words(zeros, ones):
    n = zeros + ones
    for c in combinations(range(n), ones):
        word = np.zeros(n, dtype=int)
        word[list(c)] = 1
        yield tuple(word)


def cyclic_permute(word):
    for i in range(len(word)):
        yield word[i:] + word[:i]


def dihedral_permute(word):
    return chain(cyclic_permute(word), cyclic_permute(word[::-1]))


def is_reduced(word):
    return all(word <= w for w in dihedral_permute(word))


def necklaces(n):
    return list(filter(is_reduced, binary_words(n, n)))


'''def binary_words(n):
    for c in itertools.product([0,1], repeat=n):
        word = c
        yield tuple(word)

def cyclic_permute(word):
    for i in range(len(word)):
        yield word[i:] + word[:i]

def is_reduced(word):
    return all(word <= w for w in cyclic_permute(word))

def necklaces(n):
    return list(filter(is_reduced, binary_words(n)))

'''


def srez(tupl, mesto, dlina):
    res = []
    l = len(tupl)
    for i in range(mesto, mesto + dlina):
        res.append(tupl[i % l])
    return tuple(res)


def builddict(tupl, k):
    res = {}
    for j in itertools.product([0, 1], repeat=k):
        res[j] = 0
    l = len(tupl)
    for i in range(l):
        s = srez(tupl, i, k)
        res[s] += 1
    res2 = []
    for j in itertools.product([0, 1], repeat=k):
        res2.append(res[j])
    return tuple(res2)


for n in range(1, 20):

    for k in range(1, n+1):
        listsrez = []
        for t in necklaces(n):
            listsrez.append(builddict(t, k))

        if len(listsrez) == len(set(listsrez)):
            print('for n =', n, ' k=', k)
            break
