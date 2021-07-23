from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('joinesy@example.com', '2012-05-18')
print(sub)
print(sub.addr)
print(sub.joined)

sub2 = Subscriber('123@mail.ru', '2021-07-07')
print(sub2)
print(len(sub))
sub = sub._replace(joined='2021-05-18')
print(sub)
print(sub[0] + ' ' + sub[1])

t = ['gav@gmail.com', '2020-01-15']
tn = Subscriber._make(t)
print(tn)
print(tn._asdict())
