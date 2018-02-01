# -*- coding: utf-8 -*-
'''The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
import re
from time import clock


def triangleNumbers():
    i = 1
    while True:
        yield i * (i + 1) / 2;
        i = i + 1

def char2nmbr(char):
    return ord(char) - ord('A') + 1

def isTriangleWord(word):
    n = reduce(lambda x, y: x + char2nmbr(y), word, 0)
    nmbrs = triangleNumbers()
    for i in nmbrs:
        if i == n:
            return True
        if i > n:
            return False
        
start = clock()
wordsFile = open('words.txt', 'r')
words = wordsFile.read()
words = filter(lambda x: x != '', re.split('[",]+', words))
triangleWords = filter(isTriangleWord, words)
print 'Time:   ' + str(clock() - start)
print 'Result: ' + str(len(triangleWords))
    
