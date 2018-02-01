# -*- coding: utf-8 -*-
"""A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
^(1)/_(12) , ^(2)/_(12) , ^(3)/_(12) , ^(4)/_(12) , ^(5)/_(12) , ^(6)/_(12) , ^(7)/_(12) , ^(8)/_(12) , ^(9)/_(12) , ^(10)/_(12) , ^(11)/_(12) .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = ^(4)/_(11) .
In fact, d = 12 is the smallest denominator having a resilience R(d) < ^(4)/_(10) .

Find the smallest denominator d, having a resilience R(d) < ^(15499)/_(94744) ."""
from math import sqrt;
def prime():
    primes = [2, 3]
    last = 3
    l = 0
    while True:
        last += 2
        t = [i for i in primes if last % i == 0]
        if t == []:
            primes.append(last)
            yield primes[l]
            l += 1


def is_resilient(num, denom):
    p = prime()
    for i in p:
        if (i > num):
            return True
        if (num % i == 0) and (denom % i == 0):
            return False

def denominator():
    d = 94744
    while True:
        yield d
        d += 1

d = denominator()
for i in d:
    s = 0
    for j in range(1, i):
        if is_resilient(j, i):
            s += 1
    print i            
    if (float(s) / float(i - 1)) < (float(15499) / float(94744)):
        break


    
        
