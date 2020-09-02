# range(start, stop, jump) generator
for i in range(0, 12, 3):
    print(i)
for i in range(3):
    print(i)
for i in range(1, 5):
    print(i)

# enumeration
s = 'ankit'
for idx, ch in enumerate(s):
    print(ch)
    print(idx)

# zip
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = ['a', 'b', 'c']
print(list(zip(l1, l2, l3)))
for i in zip(l1, l2, l3):
    print(i)

print('c' in ['a', 'b', 'c'])
print('p' in {'p': 1, 'q': 2, 'r': 3})
d = {'p': 1, 'q': 2, 'r': 3}
print(3 in d.values())

print(max(l1))
print(min(l2))

from random import shuffle
from random import randint
shuffle(l1)
print(l1)
print(randint(1,200))
print(randint(1,200))

a = int(input('Enter a number - '))
print(a)
s = input('Enter tour name - ')
print(s)


