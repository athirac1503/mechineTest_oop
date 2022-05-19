from turtle import width


class Area:
    width=0
    length=0
class Rectangle(Area):
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def calculatearea(self):
        print("Area of rectangle",self.length*self.width)
class Circle(Area):
    def __init__(self,length):
        self.length = length
    def calculatearea(self):
        print("Area of Circle",3.14*(self.length/2)*(self.length/2))
rectangle=Rectangle(10,20)
rectangle.calculatearea()

circle=Circle(10)
circle.calculatearea()