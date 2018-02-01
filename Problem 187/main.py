# -*- coding: cp1250 -*-
'''A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10^(8), have precisely two, not necessarily distinct, prime factors?
'''


def primes(max):
    temp = [ 1 for i in xrange(max) ]
    n = 4
    temp[0] = temp[1] = 0;
    while n < max:
        temp[n] = 0;
        n += 2;
    t = temp.index(1, 2 + 1)    
    while True:
        n = 2 * t
        while n < max:
            temp[n] = 0;
            n += t;
        try:
            t = temp.index(1, t + 1)
        except ValueError:
            break

    p = []
    for i in xrange(max):
        if temp[i] == 1:
            p.append(i);
    
    return p
    
n = 10**8
p = primes(n / 2)
print 'done'
sum = 0
for i in xrange(len(p)):
    for j in xrange(0, i + 1):
        if p[i] * p[j] < n:
            sum += 1
        else: break

print sum;
