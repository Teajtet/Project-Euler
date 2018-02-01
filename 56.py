max = 0
for i in range(100):
    for j in range(100):
        t = reduce(lambda x, y: ord(y) - ord('0') + x, str(i**j), 0)
        if (t > max): max = t

		
print max
