no = 0;
day = 1;
for i in range(1900,2001):
    for j in range(1, 13):         
        day %= 7;        
        if day == 0:
            #print "Is %i %i and 1st is in Sunday" % (i, j);
            no += 1
        if j == 4 or j == 6 or j == 9 or j == 11:
            days = 30;
        elif j == 2 and i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            days = 29;
        elif j == 2:
            days = 28;
        else:
            days = 31;
        day += days;
            
print no;
