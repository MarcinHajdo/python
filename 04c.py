import math
a = [1,2,3,4]
b= [6,7,4,2]
scalar=0
for x in range(len(a)):
    scalar = scalar + a[x]*b[x]
print(scalar)
