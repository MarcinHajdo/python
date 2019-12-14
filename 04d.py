import math
from random import randint
X = [[randint(0, 10) for x in range(8)] for y in range(8)]
Y = [[randint(0, 10) for x in range(8)] for y in range(8)]
result = [[0 for x in range(8)] for y in range(8)]
for i in range(len(X)):
  for j in range(len(Y[0])):
      for k in range(len(Y)):
          result[i][j] += X[i][k] * Y[k][j]
          
for r in result:
  print(r)
