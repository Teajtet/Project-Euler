fst = 999
sec = 999
l = []
for i in range(fst, 1, -1):
    for j in range(sec, 1, -1):
        prod = i * j;
        s = str(prod)
        ok = True  
        for k in range(len(s) // 2):
            if s[k] != s[-k - 1]:
                ok = False
        if ok:
            l.append(prod)

print max(l)
