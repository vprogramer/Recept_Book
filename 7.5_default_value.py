# default value for list
def spam1(a, b=None):
    if b is None:
        b = []
    b.append(a)
    return b


print(spam1(3, spam1(2, spam1(1, []))))

# 2
_no_value = object()


def spam2(a, b=_no_value):
    if b is _no_value:
        print('No b value')
        return None
    return a+b


print(spam2(1))
print(spam2(1, 2))

# 3
x = 42


def spam3(a, b=x):
    print(a, b)


spam3(1)
x = 25
spam3(2)