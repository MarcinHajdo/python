import math
from random import randint
randoms = [randint(0, 100) for p in range(0, 50)]
randoms_copy = randoms
for x in range(len(randoms)):
    for y in range(len(randoms) - 1):
        if randoms[y] < randoms[y+1]:
            temp = randoms[y]
            randoms[y] = randoms[y+1]
            randoms[y+1] =temp
print(randoms == sorted(randoms_copy,reverse=True))
