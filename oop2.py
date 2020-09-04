class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def circumference(self):
        return (2 * self.radius * Circle.pi)


c = Circle()
c1 = Circle(radius=5)
print(c.pi)
print(c.radius)
print(c1.radius)
print(c.circumference())
print(c1.circumference())
print(c.area)
print(c1.area)