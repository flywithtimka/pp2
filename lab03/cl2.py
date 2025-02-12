class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        """Returns the area of the square (length * length)."""
        return self.length * self.length

length = float(input("Enter the number"))
square = Square(length)
print(f"{square.area()}")  