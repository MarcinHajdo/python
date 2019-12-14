import os
for r, d, f in os.walk("C:/"):
    for file in f:
       print(file)
