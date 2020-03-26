class Rectangle:
    def __init__(self, len, breadth):
        self.len = a
        self.breadth = b

    def area(self):
        return self.breadth * self.len
    
    def perimeter(self):
        return (self.breadth + self.len) * 2

x = input()
a = int(x.split()[0])
b = int(x.split()[1])
rectangle = Rectangle(a, b)
print(str(rectangle.area() )+ " " +str(rectangle.perimeter()))