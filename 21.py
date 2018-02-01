"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ? b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

from math import sqrt, floor;

def sumOfDivisors(nmbr):
    sum = 0;
    for i in range(2, int(floor(sqrt(nmbr))) + 1):
        if nmbr % i == 0:
            sum += i;
            if nmbr / i != i:
                sum += nmbr / i;
    return sum + 1;
			
maxNmbr = 10000;
tab = [0]*maxNmbr;
for i in range(2,maxNmbr):
    tab[i] = sumOfDivisors(i);

sum = 0;
for i in range(1,maxNmbr):
    if tab[i] < maxNmbr and tab[tab[i]] == i and tab[i] != i:
        print i
        sum += i;
	
print sum
