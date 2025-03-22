from abc import ABC, abstractmethod  # Import ABC module for abstract classes


# Define an abstract base class FileHandler
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass  # Placeholder for the read method

    @abstractmethod
    def write(self, data):
        pass  # Placeholder for the write method


# Define a concrete class for text file handling
class TextFileHandler(FileHandler):
    def read(self):
        return "Reading text file..."  # Implementing the read method

    def write(self, data):
        return f"Writing '{data}' to text file..."  # Implementing the write method


# Define a concrete class for binary file handling
class BinaryFileHandler(FileHandler):
    def read(self):
        return "Reading binary file..."  # Implementing the read method

    def write(self, data):
        return f"Writing binary data: {data}"  # Implementing the write method


# Create instances of TextFileHandler and BinaryFileHandler
text_handler = TextFileHandler()
binary_handler = BinaryFileHandler()

# Test the methods
print(text_handler.read())  # Output: Reading text file...
print(text_handler.write("Hello"))  # Output: Writing 'Hello' to text file...
print(binary_handler.read())  # Output: Reading binary file...
print(binary_handler.write(b'101010'))  # Output: Writing binary data: b'101010'