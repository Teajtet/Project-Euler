def prime():
    primes = [2, 3]
    last = 3
    while True:
        last += 2
        t = [i for i in primes if last % i == 0]
        if t == []:
            primes.append(last)
            yield (last, len(primes))
p = prime()
while True:
    (val, no) = p.next()
    if no == 10001:
        print(val)
        break
