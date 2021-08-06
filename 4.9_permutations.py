from itertools import permutations


items = ['a', 'b', 'c']
for p in permutations(items, 3):
    print(p)


for p in permutations(items, 2):
    print(p)


from itertools import combinations


for c in combinations(items, 3):
    print(c)