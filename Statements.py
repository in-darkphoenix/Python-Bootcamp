print('Welcome to the python statements')

# Conditional
name = 'Ankit'
if name == 'Altair':
    print('Welcome to the Masyaf Temple')
elif name == 'Ezio':
    print('Welcome to Italy')
elif name == 'Connor':
    print('Welcome to America')
elif name == 'Edward':
    print('Welcome to Caribbean')
else:
    print('Not played')

# Iteration 'for'
mylist = [1, 2, 3, 4, 5]
for num in mylist:
    print(num)
for _ in mylist:
    print('Sorry')

nl = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for item in nl:
    print(item)
for a, b, c in nl:
    print(b)
    print(a)
    print(c)

d = {'k1': 'hello', 'k2': 2.9, 'k3': True}
for i in d:
    print(i)
for k, v in d.items():
    print(v)
for v in d.values():
    print(v)

for n in mylist:
    if n % 2 == 0:
        print(f'Even {n}')
    else:
        print(f'Odd {n}')

# Iteration 'while'
x = 9
while x <= 4:
    print(x)
    x += 1
else:
    print('x in greater than 5')

# break, continue, pass
for i in 'Hello':
    pass

x = 8
while x < 12:
    if x == 10:
        break
    print(x)
    x += 1

x = 9
while x < 15:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

























