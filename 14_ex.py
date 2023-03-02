class Square:
    square_list = []

    def __init__(self,l):
        self.len = l
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by{}".format(self.len,self.len,self.len,self.len)

new1 = Square(10)
print(Square.square_list)

new2 = Square(20)
print(Square.square_list)

new3 = Square(30)
print(new3)
print(Square.square_list)


def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "b"))