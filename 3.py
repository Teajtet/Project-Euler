def primes():
    i = 1
    while True:
        prime = True;
    for j in range(2, i):
            if i % j == 0:
                prime = False;
                break
            if prime:
                yield i
            i += 1

p = primes()
for i in p:
    if 600851475143L % i == 0:
        print i
    if i > 600851475143L:
        break
