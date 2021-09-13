# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 00:25:15 2021

@author: beelzebub
"""

import itertools as it
import numpy as np

def tabl(t):
    (a,b)=np.shape(t)
    if a==0:
        return 0
    if b==0:
        return 0
    if b==1:
        if 1 in t[:,0]:
            return 1
        else:
            return np.Inf
    o=[ np.Inf ]
    for i in range(a):
        el = t[i,:]
        el_ind = np.where(el)[0]
        if el_ind.size==0:
            continue
        o = o + [1 + tabl(np.delete(t, el_ind, 1))]
    return min(o)

'''
testar = np.array([1,0,0,1,1,1,1,1])
testar = np.reshape(testar, (2,4))
print(tabl(testar))
'''

def findrot(m):
    n=len(m)*2
    t = np.empty((0,n))
    l = [0]*n
    for j in m:
        l[j] = 1
    for i in range(n):
        ad =l[i:] + l[:i]
        t = np.vstack([t, ad])
    return tabl(t)


print(findrot((0,2)))

def go(n):
    otv = 0
    for i in it.combinations(range(n), n//2):
        otv = max(findrot(i), otv)
        #print(findrot(i), i)
    print("n = ", n, "otv = ", otv)


for nh in range(100):
    n=2*nh
    go(n)
