import os
my_file = 'my_file.jpg'
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.png')
