def sortChar(string):
    temp = []
    for char in string:
        temp.append(char)
    temp.sort()
    return temp

i = 1;
done = False
while not done:
    i1 = sortChar(str(i))
    i2 = sortChar(str(2*i))
    i3 = sortChar(str(3*i))
    i4 = sortChar(str(4*i))
    i5 = sortChar(str(5*i))
    i6 = sortChar(str(6*i))
    if i1 == i2 and i1 == i3 and i1 == i4 and i1 == i5 and i1 == i6:
        print i
        done = True;
    i += 1
