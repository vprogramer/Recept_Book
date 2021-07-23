import time

hundred = list(range(1000000))
gen_start = time.time()
s1 = sum(x * x for x in hundred)
gen_stop = time.time()
print(gen_stop - gen_start)

list_start = time.time()
s2 = sum([x * x for x in hundred])
list_stop = time.time()
print(list_stop - list_start)


nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# Сокращение (reduction) данных по полям в структуре данных
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)