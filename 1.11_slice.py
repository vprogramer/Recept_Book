record = '....................100 .......513.25 ..........'
cost = int(record[20:22]) * float(record[31:37])

print(cost)

SHARES = slice(20, 22)
PRICE = slice(31, 37)

cost2 = int(record[SHARES]) * float(record[PRICE])
print(cost2)

