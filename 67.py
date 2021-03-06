'''By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^(99) altogether! If you could check one trillion (10^(12)) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)'''

f = open('triangle.txt', 'r')
string = f.read()
t = string.split('\n')
t = map(lambda x: x.split(' '), t)
i = 0
max = [0]*(len(t)+1)
for i in range(len(t) - 1, -1, -1):
    temp = []
    for j in range(i + 1):
        temp.append((lambda x, y: x > y and x or y)(max[j], max[j+1])+int(t[i][j]))
    max = temp

print max
