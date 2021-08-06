items = [1, 2, 3]

it = iter(items)

try:
    while True:
        print(next(it))
except StopIteration:
    pass

print("---")

it = iter(items)

while True:
    num = next(it, None)
    if num is None:
        break
    print(num)
