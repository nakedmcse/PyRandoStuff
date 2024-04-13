import math

# Base shape class
class shape:
    def __init__(self):
        self.height = 0.0
        self.width = 0.0
        self.radius = 0.0

    def area(self):
        return 0


# Circle
class circle(shape):
    def area(self):
        return math.pi * self.radius * self.radius

    def getparams(self):
        self.radius = float(input("Enter Radius:"))


# Rectangle
class rectangle(shape):
    def area(self):
        return self.width * self.height

    def getparams(self):
        self.width = float(input("Enter Width:"))
        self.height = float(input("Enter Height:"))


# Triangle
class triangle(shape):
    def area(self):
        return self.width * self.height * 0.5

    def getparams(self):
        self.width = float(input("Enter Base Length:"))
        self.height = float(input("Enter Height:"))


# Main
shapetype = input("Enter Shape Type:")
if shapetype not in globals():
    print("Shape not defined")
    exit(1)
shapeObject = globals()[shapetype]()
shapeObject.getparams()
print("Area", shapeObject.area())