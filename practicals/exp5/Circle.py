class Circle:
    def __init__(self, ):
        self.setRadius()
        self.PI = 3.14


    def setRadius(self, ):
        self.radius = int(input("Enter the radius of a circle: "))


    def findArea(self, ):
        area = self.PI*self.radius**2
        print ("Area of cirlce is: ", area)

    def findCircumference(self, ):
        circumference = 2*self.PI*self.radius
        print ("Circumference of cirlce is: ", circumference)


c1 = Circle()
c1.findArea()
c1.findCircumference()