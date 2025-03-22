# Define a Dog class
class Dog:
    def make_sound(self):
        return "Woof!"  # Dog's sound

# Define a Cat class
class Cat:
    def make_sound(self):
        return "Meow!"  # Cat's sound

# Define a function that processes any object with a make_sound method
def process_sound(sound_object):
    return sound_object.make_sound()

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call process_sound with both objects
print(process_sound(dog))  # Output: Woof!
print(process_sound(cat))  # Output: Meow!