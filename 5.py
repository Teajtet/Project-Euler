li = range(2, 21)

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if (li[j] %  li[i] == 0):
            li[j] /= li[i]

        
print reduce(lambda x, y: x*y, li, 1)
print li

