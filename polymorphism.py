class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says meow!"


class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says woof!"

c = Cat("Yuni")
d = Dog("Daisy")
print(c.speak())
print(d.speak())

def speak(pet):
    print(pet.speak())

speak(c)
speak(d)