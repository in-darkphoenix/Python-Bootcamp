file = open('hw.txt')
print(file.read())
print(file.read())
print(2)
file.seek(0)
print(file.read())
file.seek(0)
print(file.readlines())

nfile = open('hello.txt')
print(nfile.read())
nfile.seek(0)
print(nfile.readlines())
