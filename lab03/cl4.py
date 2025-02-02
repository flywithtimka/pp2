class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

 
p1 = Point(3, 4)
p2 = Point(6, 8)

p1.show()   
p2.show()   

print(p1.dist(p2))   

p1.move(10, 12)
p1.show()   
