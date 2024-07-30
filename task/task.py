import os
from contextlib import contextmanager


# Part 1 - Basic Error Handling
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileProcessingError(f"File not found: {file_path}")
    except IOError as e:
        raise FileProcessingError(f"IO Error while reading file: {e}")


# Part 2 - Handling Multiple Exceptions
def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        raise FileProcessingError(f"IO Error while writing to file: {e}")
    except PermissionError:
        raise FileProcessingError(f"Permission denied: Unable to write to {file_path}")
    else:
        print(f"Successfully wrote to {file_path}")


# Part 3 - Custom Exceptions
class FileProcessingError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Part 4 - Using Context Managers
@contextmanager
def FileHandler(file_path, mode):
    file = None
    try:
        file = open(file_path, mode)
        yield file
    except IOError as e:
        raise FileProcessingError(f"Error handling file {file_path}: {e}")
    finally:
        if file:
            file.close()


# Part 5 - Putting It All Together
def file_processing_system():
    while True:
        file_path = input("Enter the file path: ")
        operation = input("Enter the operation (read/write): ").lower()

        try:
            if operation == 'read':
                with FileHandler(file_path, 'r') as file:
                    content = file.read()
                print(f"File content:\n{content}")
            elif operation == 'write':
                content = input("Enter the content to write: ")
                with FileHandler(file_path, 'w') as file:
                    file.write(content)
                print(f"Successfully wrote to {file_path}")
            else:
                print("Invalid operation. Please enter 'read' or 'write'.")
        except FileProcessingError as e:
            print(f"Error: {e}")

        continue_processing = input("Do you want to process another file? (yes/no): ").lower()
        if continue_processing != 'yes':
            break


# Run the file processing system
if __name__ == "__main__":
    file_processing_system()
