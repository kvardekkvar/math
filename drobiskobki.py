# -*- coding: utf-8 -*-

from math import gcd


# the program counts and prints all rational numbers obtained by placing parenthesis in expression a_1 / a_2 / a_3 / ... / a_n , where '/' is the division sign

class Rational():
    def __init__(self, p, q=1):
        self.p = p // int(gcd(p, q))
        self.q = q // int(gcd(p, q))
        if (self.q < 0):
            self.p, self.q = -self.p, -self.q
        assert self.q != 0
        self.value = p/q

    def __add__(self, other):
        new_p = self.p * other.q + self.q * other.p
        new_q = self.q * other.q
        new_p, new_q = new_p//int(gcd(new_p, new_q)), new_q//int(gcd(new_p, new_q))
        if (new_q < 0):
            new_p, new_q = -new_p, -new_q
        assert new_q != 0
        return Rational(new_p, new_q)

    def __sub__(self, other):
        return self + Rational(other.p * (-1), other.q)

    def __mul__(self, other):
        new_p = self.p*other.p
        new_q = self.q*other.q
        new_p, new_q = new_p // int(gcd(new_p, new_q)), new_q // int(gcd(new_p, new_q))
        if (new_q < 0):
            new_p, new_q = -new_p, -new_q
        assert new_q != 0
        return Rational(new_p, new_q)

    def __truediv__(self, other):
        return self * Rational(other.q, other.p)


a = [Rational(y) for y in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                           97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]]
len = 9
a = a[:len]


def fractions_generator(n, a):
    if (n == 2):
        yield a[0]/a[1]
    for i in range(n-1):
        new_a = a[:i] + [(a[i]/a[i+1])] + a[i+2:]
        yield from fractions_generator(n-1, new_a)


result_set = set()
for fraction in fractions_generator(len, a):
    result_set.add((fraction.p, fraction.q))

print(len(result_set), result_set)
