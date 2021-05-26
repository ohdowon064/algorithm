from functools import reduce
import random as rd
a = list(range(1, 10))

n = reduce(lambda x, y: 10 * x + y, a, 1)
print(n)
