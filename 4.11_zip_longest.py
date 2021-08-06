from itertools import zip_longest


a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']

for i in zip_longest(a, b, fillvalue="Hi"):
   print(i)