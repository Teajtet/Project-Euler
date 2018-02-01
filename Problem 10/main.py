"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
from math import ceil, sqrt
primes = range(2, 2000000)

j = 2
#print i
while True:      
    j += 2
    if (j >= 2000000):
        break
    primes[j - 2] = 0           

for i in range(3, ceil(sqrt(int(2000000))), 2):
    j = i
    #print i
    while True:      
        j += i
        if (j >= 2000000):
            break
        primes[j - 2] = 0
        

print sum(primes)
