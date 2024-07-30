import unittest
from task.task import read_file, FileProcessingError


class TestFileProcessing(unittest.TestCase):
    def test_read_file_success(self):
        # Create a temporary file with content
        with open("test_file.txt", "w") as f:
            f.write("Test content")

        content = read_file("test_file.txt")
        self.assertEqual(content, "Test content")

    def test_read_file_not_found(self):
        with self.assertRaises(FileProcessingError):
            read_file("nonexistent_file.txt")

    # Add more test cases for read_file, write_file, and FileHandler


if __name__ == '__main__':
    unittest.main()
