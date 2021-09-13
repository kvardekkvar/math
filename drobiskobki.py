# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:23:25 2021

@author: beelzebub
"""
from math import gcd

class pq():
    def __init__(self, p, q=1):
        self.p = p// int(gcd(p,q))
        self.q = q // int(gcd(p,q))
        if(self.q<0): 
            self.p, self.q = -self.p, -self.q
        assert self.q != 0
        self.v = p/q
        
    def __add__(self, other):
        pp = self.p*other.q + self.q * other.p
        qq = self.q*other.q
        pp, qq = pp//int(gcd(pp,qq)), qq//int(gcd(pp,qq))
        if(qq<0): 
            pp, qq = -pp, -qq
        assert qq != 0
        return pq(pp,qq)

    def __sub__(self, other):
        return self + pq(other.p * (-1), other.q)
    def __mul__(self, other):
        pp = self.p*other.p
        qq = self.q*other.q
        pp, qq = pp//int(gcd(pp,qq)), qq//int(gcd(pp,qq))
        if(qq<0): 
            pp, qq = -pp, -qq
        assert qq != 0
        return pq(pp,qq)

    def __truediv__(self, other):
        return self * pq(other.q, other.p)
m = [pq(y) for y in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]]
n=9
m = m[:n]

def gegege(n, m):
        if (n==2):
            yield m[0]/m[1]
        for i in range(n-1):
            mym=m[:i] + [(m[i]/m[i+1])] + m[i+2:]
            yield from gegege(n-1, mym)
            
s = set()
for i in gegege(n, m):
        s.add( (i.p, i.q))

print(len(s), s)