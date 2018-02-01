def count(pennies, nominals):
    global results
    if pennies <= 1:
        return 1
    if results[len(nominals)][pennies] != 0:
        return results[len(nominals)][pennies]
    res = 0
    for i in range(len(nominals)):
        if nominals[i] <= pennies:
           res += count(pennies - nominals[i], nominals[:i+1])
    results[len(nominals)][pennies] = res
    return res

pennies = 200
nominals = [1, 2, 5, 10, 20, 50, 100, 200]
results = [[0 for i in range(pennies + 1)] for j in range(len(nominals) + 1)]
print count(pennies, nominals);
