from math import floor, sqrt

i = 1
k = 1
done = False

while not done:
    s = sum([ i % j == 0 for j in range(1, int(floor(sqrt(i))) + 1)])
    if s > 250:
        print i
        done = True
    k += 1
    i += k
