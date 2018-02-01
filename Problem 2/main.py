def fibb():
	i = 1
	j = 1
	while True:                		
		(i, j) = (j+i, i)
		yield j
f = fibb()
print sum([i for i in f if (i % 2 == 0)])
