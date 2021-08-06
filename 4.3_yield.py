def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 15, 0.5):
    print(n)


it = frange(0, 1, 0.3)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
