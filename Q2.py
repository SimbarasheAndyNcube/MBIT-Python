import math  # Import math module for pi


# Define a base class Shape
class Shape:
    def area(self):
        return 0  # Placeholder method


# Define a Circle class that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  # Calculate area of a circle


# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Calculate area of a rectangle


# Function to calculate total area of all shapes in a list
def total_area(shapes):
    return sum(shape.area() for shape in shapes)  # Calls area() for each shape


# Create a list of shapes
shapes = [Circle(5), Rectangle(4, 6)]

# Calculate and print total area
print(total_area(shapes))  # Output: Sum of areas