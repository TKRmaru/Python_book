import math


class Apple:
    def __init__(self, w, c, o, d):
        self.weight = w
        self.color = c
        self.original = o
        self.date = d


apple = Apple(100, "pink", "Aomori", 10)
print(apple.color)


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi


circle = Circle(10)
print(circle.area())


class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h

    def area(self):
        return self.bottom * self.height / 2


triangle = Triangle(20, 10)
print(triangle.area())


class Hexagon:
    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return self.length * 6


hexagon = Hexagon(10)
print(hexagon.calculate_perimeter())