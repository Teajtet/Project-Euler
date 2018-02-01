d = { 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, "hundred":len("hundred"), "and":len("and"), "thousand":len("thousand")}
def countLetters(number):
    if number <= 20:
        return d[number]
    if number < 100:
        temp = 0
        if number % 10 != 0:
            temp = d[number % 10]
        return d[number - number % 10] + temp
    if number < 1000:
        temp = 0;
        if number % 100 != 0:
            temp += d["and"] + countLetters(number % 100)
        return d[number / 100] + d["hundred"] + temp
    return d[1] + d["thousand"]

print sum([countLetters(i) for i in xrange(1, 1001)])
