print("Welcome to the lists operation procedure")

ml = [1, 2, 3]
print(ml)
ml = ['Hello', 2, 5.64]
print(ml)
print(ml[2])
print(ml[1:])
al = ['hi', 46.3, 22.9, "bi"]
print(ml + al)

nl = ml + al
nl[3] = 79
print(nl)
nl.append('Ankit')
print(nl)
print(nl.pop())
nl.pop(3)
print(nl)

sl = ['q', 'u', 'i', 'c', 'k']
nl = [66, 52, 47, 2, -778, -2]
sl.sort()
nl.sort()
print(sl)
print(nl)

sl.reverse()
nl.reverse()
print(sl)
print(nl)
