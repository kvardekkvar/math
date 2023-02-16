# -*- coding: utf-8 -*-

# the program counts nxm table permutations such that each element is in the same row or column

import itertools
import numpy as np
import math

n = 20
t = np.zeros((n, n), dtype=object)
tt = np.zeros((n, n), dtype=object)
for i in range(n):
    for j in range(n):
        add = np.zeros((n, 1))
        if i == 0 or j == 0:
            add[i+j] = 1
        else:
            for k in range(n):
                add[k] = t[i-1, j][k]+t[i, j-1][k]
        t[i, j] = add

for i in range(n):
    for j in range(n):
        tt[i, j] = np.transpose(t[i, j])


def list_sum(l1, l2):
    assert len(l1) == len(l2)
    result = np.zeros(len(l1))
    for i in range(len(l1)):
        result[i] = l1[i]+l2[i]
    return result


def list_product(l1, l2):
    assert len(l1) == len(l2)
    result = np.zeros(len(l1))
    for i in range(len(l1)):
        a = l1[i]
        if a == 0:
            a = 1
        b = l2[i]
        if b == 0:
            b = 1
        result[i] = a*b
    return result


def degree(p):
    k = 0
    for i in range(1, len(p)+1):
        if p[-i] != 0:
            return len(p)-i


def polynomials_product(l1, l2):
    result = []
    for c in range(degree(l1) + degree(l2) + 1):
        coefficient = 0
        for i in range(c+1):
            if c-i <= degree(l1) and i <= degree(l2):
                coefficient += l1[c-i]*l2[i]
        result.append(coefficient)
    return result


def polynomials_sum(p1, p2):
    result = []
    if degree(p1) == None:
        return p2
    if degree(p2) == None:
        return p1
    for c in range(max(degree(p1)+1, degree(p2)+1)):
        if c <= degree(p1) and c <= degree(p2):
            coefficient = p1[c] + p2[c]
        elif c <= degree(p1):
            coefficient = p1[c]
        elif c <= degree(p2):
            coefficient = p2[c]
        else:
            coefficient = 0
        result.append(coefficient)
    return result


p1 = (1, -1, 1)
p2 = (5, 0)
print(polynomials_sum(p1, p2))

'''
p1= (1,-1,1)
p2= (5,0)
print(prodpolynom(p1, p2))
'''
'''
res=[] 
for k in range(n):
    srow=np.zeros((n,1))
    for i in range(k):
        srow= sumlist(t[i,k-i], srow)
    res.append(srow)
    
resprod=[] 
for k in range(n):
    srow=np.zeros((n,1))
    for i in range(k):
        srow= prodlist(t[i,k-i], srow)
    resprod.append(srow)
'''


def polynomial_formula(p):
    s = ''
    if degree(p) == None:
        return '0'
    for i in range(degree(p)+1):
        if p[i] != 0:
            s += str(int(p[i])) + 'x^'+str(i)+'+'
    return s


def value(p, x):
    result = 0
    if (degree(p) == None):
        return 0
    for i in range(degree(p)+1):
        result += (int(p[i])*(x**i))
    return result


result = []
for k in range(n):
    spp = np.zeros((n, 1))
    for i in range(k+1):
        xk = np.zeros((n, 1))
        xk[i] = 1
        add = polynomials_product(t[i, k-i], xk)
        spp = polynomials_sum(spp, add)
    result.append(spp)


def fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a


result_pretty = [polynomial_formula(p) for p in result]
# resval = [value(p, 2**0.5) for p in res]

i = 0
result_values = []
for p in result:

    result_values.append(value(p, i))
    i += 1
