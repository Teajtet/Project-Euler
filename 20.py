# -*- coding: utf-8 -*-
'''n! means n × (n − 1) × ... × 3 × 2 × 1

Find the sum of the digits in the number 100!'''


print reduce(lambda x, y: x + int(y), str(reduce(lambda x, y: x * y, range(2, 100), 1)), 0)
