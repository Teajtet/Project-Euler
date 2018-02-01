# -*- coding: cp1250 -*-
'''Starting in the top left corner of a 2×2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20×20 grid?'''

maxx = 20
maxy = 20
x = 0
y = 0
number = 0;

def slow_find(x, y):
    global number
    if (x == maxx) and (y == maxy):
        number += 1
    if  x < maxx:
        slow_find(x+1, y)
    if  y < maxy:
        slow_find(x, y+1)
    return

temp = [0]*((maxx+1)*(maxy+1))

def fast_find(x, y):
    if x == 1:
        return y + 1
    if temp[x*maxx+y] == 0:
        i = fast_find(x - 1, y)
        if y - 1 < x:
            i += fast_find(y - 1, x)
        else:
            i += fast_find(x, y - 1)
        temp[x*maxx+y] = i
        return i
    else:
        return temp[x*maxx+y]

#slow_find(0, 0)
#print number
print fast_find(maxx, maxy)
print temp
