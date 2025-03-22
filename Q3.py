# Define a base class Shape
class Shape:
    def __init__(self):
        print("Initializing Shape")  # This message will be printed when Shape is initialized

    def calculate_area(self):
        return 0  # Placeholder method


# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()  # Calls the constructor of the parent class (Shape)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height  # Calculate area of rectangle


# Create an instance of Rectangle
rect = Rectangle(4, 6)

# Print the area
print(rect.calculate_area())  # Output: 24