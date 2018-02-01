for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            for l in range(0, 10):
                for m in range(0, 10):
                    for n in range(0, 10):
                        for o in range(0, 10):
                            if i**5 + j**5 + k**5 + l**5 + m**5 + n**5 + o**5 == i*1000000 + j*100000 + k*10000 + l*1000 + m*100 + n*10 + o:
                                print "%i%i%i%i%i%i%i" % (i, j, k, l, m, n, o)
        
