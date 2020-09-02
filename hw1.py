import math as m

class Line():

    def __init__(self, coor1, coor2):
        self.c1 = coor1
        self.c2 = coor2

    def dist(self):
        x1, y1 = self.c1
        x2, y2 = self.c2
        #d = m.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        return d

    def slope(self):
        x1, y1 = self.c1
        x2, y2 = self.c2
        s = (y1 - y2)/(x1 - x2)
        return s


coordinate1 = (3,2)
coordinate2 = (8,10)
l = Line(coordinate1,coordinate2)
print(l.dist())
print(l.slope())


class Cylinder():

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.h = height
        self.r = radius

    def volume(self):
        v = self.pi * (self.r**2) * self.h
        return v

    def surface_area(self):
        sa = (2 * self.pi * self.r) * (self.h + self.r)
        return sa


c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())

































