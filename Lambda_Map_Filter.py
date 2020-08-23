print('Welcome to the map, filter function and lambda expression centre.')


def cubes(n):
    return n ** 3


l = [1, 2, 3, 4, 5]
for i in map(cubes, l):
    print(i)


def check_odd(n):
    return n % 2 != 0


print(list(filter(check_odd, l)))

print(list(map(lambda n: n ** 3, l)))

print(list(filter(lambda n: n % 2 != 0, l)))

s = ['victor', 'sara', 'andy', 'carlo']
print(list(map(lambda x: x[0], s)))
