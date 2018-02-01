lst = []
for i in xrange(2, 101):
    for j in xrange(2, 101):
        lst.append(i ** j)

list.sort(lst)
l = 0
c = 0
for i in lst:
    if i != l:
        l = i
        c = c + 1

print c
