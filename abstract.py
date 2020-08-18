# we should not instantiate the abstract class, subclasses implements its functions only

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Cat(Animal):

    def speak(self):
        return f"{self.name} says meow!"


class Dog(Animal):

    def speak(self):
        return f"{self.name} says woof!"


c = Cat("Soni")
print(c.speak())

d = Dog("Daisy")
print(d.speak())