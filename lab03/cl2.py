class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        """Returns the area of the square (length * length)."""
        return self.length * self.length

 
shape = Shape()
print("Shape area:", shape.area())   

square = Square(5)
print("Square area:", square.area())  