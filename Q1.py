# Define a base class called Vehicle
class Vehicle:
    def start(self):
        return "Vehicle is starting..."

# Define a subclass called Car that inherits from Vehicle
class Car(Vehicle):
    def start(self):  # Overriding the start method
        return "Car is starting with a roar!"

# Define a subclass called Bike that also inherits from Vehicle
class Bike(Vehicle):
    def start(self):  # Overriding the start method
        return "Bike is starting with a vroom!"

# Create instances of Car and Bike
car = Car()
bike = Bike()

# Call the start method on both objects
print(car.start())  # Output: Car is starting with a roar!
print(bike.start())  # Output: Bike is starting with a vroom!
