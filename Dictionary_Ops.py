print('Hello, I welcome to the dictionaries operation procedure')

d = {'ac2': 9.99, 'gta5': 25.5, 'pubg': 4.55}
print(d)
print(d['pubg'])

d1 = {'k1': 123, 'k2': [0, 'hello', 2.9], 'k3': {'ik': "bi"}}
print(d1)
print(d1['k1'])
print(d1['k2'])
print(d1['k3'])
print(d1['k3']['ik'])
print(d1['k2'][2])

d2 = {'k1': 1, 'k2': ['a', 'b', 'c']}
print(d2)
print(d2['k2'][1].upper())
d2['k3'] = 6.9
print(d2)
d2['k2'][2] = 'C'
print(d2)

print(d1.keys())
print(d1.values())
print(d1.items())

