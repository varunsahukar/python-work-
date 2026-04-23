"""
Topic 14: Introduction to Testing
=================================
Covers: unittest module, creating a test case, assertions
"""
import unittest

# --- The code to be tested ---

def add(a, b):
    """A simple function to add two numbers."""
    return a + b

def subtract(a, b):
    """A simple function to subtract two numbers."""
    return a - b

# --- The tests ---

class TestMathFunctions(unittest.TestCase):
    """A test case for our math functions."""

    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(-1, 1), -2)

# To run the tests, you would typically run this from the command line:
# python -m unittest topic14_introduction_to_testing.py

if __name__ == '__main__':
    # This allows you to run the tests by running the script directly
    unittest.main()