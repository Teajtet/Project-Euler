# -*- coding: cp1250 -*-
'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

from time import clock

def findDivisors(nmbr):
    i = 2
    while i * i < nmbr:
        if nmbr % i == 0:
            yield (i, nmbr / i)
        i = i + 1

minVal = 1000
maxVal = 99999
result = []

start = clock()
for i in xrange(minVal, maxVal):
    for (a, b) in findDivisors(i):
        nmbr2list = lambda x: list(str(x))
        digits = nmbr2list(i) + nmbr2list(a) + nmbr2list(b)
        uniqueDigits = list(set(digits));
        if len(digits) == 9 and len(uniqueDigits) == 9:
            noZeros = True
            for digit in digits:
                if digit == '0':
                    noZeros = False

            if noZeros:
                result.append(i)
                break

print "time:   " + str(clock() - start)
print "result: " + str(sum(result))
