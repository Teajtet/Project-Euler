z = 10**6-1
x = 9*8*7*6*5*4*3*2*1
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9,0,-1):
    print list.pop(z / x)
    y = (z / x) * x
    z -= y
    x /= i
print z / x
