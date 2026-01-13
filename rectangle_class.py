class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print("The length is " + str(self.length) + "\nThe width is " + str(self.width) + "\nThe area is " + str(self.length * self.width))
    def perimeter(self):
        print("The perimeter is " + str((self.width * 2) + (self.length * 2)))

r1 = Rectangle(10,9)
r1.area()
r1.perimeter()
        