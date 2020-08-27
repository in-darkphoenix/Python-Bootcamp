print('welcome to the list comprehension procedure')

s = 'ankit'
l = []
for ch in s:
    l.append(ch)
print(l)

s1 = 'cat'
l1 = [x for x in s1]
print(l1)

l2 = [x for x in range(5)]
print(l2)

l2 = [x ** 3 for x in range(5)]
print(l2)

l2 = [x ** 2 for x in range(10) if x % 2 != 0]
print(l2)

c = [0, 100.0, -40.0, -273, 27, 104]
f = [(9 / 5) * t + 32 for t in c]
print(f)

l2 = [x if x % 2 != 0 else 'even' for x in range(10)]
print(l2)

l2 = [x * y for x in [1, 2, 3] for y in [1, 10, 100]]
print(l2)
