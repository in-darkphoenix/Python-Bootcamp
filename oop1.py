class Sample():
    pass

instanceofclass = Sample()
print(type(instanceofclass))

class Cat():

    species = 'mammals'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    
    def meow(self, age):
        print(f'Maaeo! My name is {self.name} and I am {age} years old')

mycat = Cat(breed='munchkin', name='Xuni')
print(mycat.breed, " ", mycat.name)
print(mycat.species)
mycat.meow(2)