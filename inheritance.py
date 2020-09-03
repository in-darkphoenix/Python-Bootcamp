class Animal():

    def __init__(self):
        print('ANIMAL created....!')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating now')

#a = Animal()
#a.who_am_i()
#a.eat()

class Cat(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Cat created...!')

    # override
    def who_am_i(self):
        print('I am a cat!')

    def mew(self, name):
        print(f'Meawww! my name is {name}')

c = Cat()
c.who_am_i()
c.eat()
c.mew(name='Soni')