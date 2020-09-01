print('Hi, welcome to the tuples procedure operation')

t = (1, 2.9, "hello")
print(type(t))
print(t)
print(t[2])
print(len(t))
print(t[-2])

t1 = (1, 2, 2, 2, 4.9)
print(t1)
print(t1.count(2))
print(t1.index(4.9))

l = [1, 2]
print(l)
l[1] = 'b'
print(l)
#t1[3] = 8  #tuple is immutable
print(t1)
