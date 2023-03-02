class Shape:
    def what_am_i(self):
        print("I am shape")


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2


class Square(Shape):
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len * 4

    def change_size(self, new_size):
        self.len += new_size

rectangle = Rectangle(10, 20)
print(rectangle.calculate_perimeter())

square = Square(10)
print(square.calculate_perimeter())
square.change_size(2)
print(square.calculate_perimeter())

rectangle.what_am_i()
square.what_am_i()


class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

rider = Rider("NERO")
horse = Horse("Hachi",rider)
print(horse.owner.name)