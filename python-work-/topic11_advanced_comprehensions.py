"""
Topic 11: Advanced Comprehensions
=================================
Covers: dict comprehensions, set comprehensions, nested comprehensions
"""

# ─────────────────────────────────────────
# 1. Dictionary Comprehensions
# ─────────────────────────────────────────
# Create a dictionary from lists of keys and values
keys = ["name", "city", "role"]
values = ["Arjun", "Mumbai", "Developer"]

user_profile = {keys[i]: values[i] for i in range(len(keys))}
print(f"User Profile from lists: {user_profile}")

# Create a dictionary from an existing one, with a condition
user_data = {"name": "Arjun", "age": 25, "experience_years": 3}
senior_check = {key: value for key, value in user_data.items() if isinstance(value, int) and value > 5}
print(f"Senior Check: {senior_check}") # Empty because no int value is > 5

# Swap keys and values
original_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = {v: k for k, v in original_dict.items()}
print(f"Swapped Dictionary: {swapped_dict}")


# ─────────────────────────────────────────
# 2. Set Comprehensions
# ─────────────────────────────────────────
# Create a set of unique squared numbers from a list with duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {n**2 for n in numbers}
print(f"Unique Squares: {unique_squares}")

# Create a set of the first letter of each word in a sentence
sentence = "the quick brown fox jumps over the lazy dog"
first_letters = {word[0] for word in sentence.split()}
print(f"First Letters: {first_letters}")


# ─────────────────────────────────────────
# 3. Nested Comprehensions
# ─────────────────────────────────────────
# Create a flattened list from a list of lists (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [cell for row in matrix for cell in row]
print(f"Flattened Matrix: {flattened}")

# Create a list of coordinates where the sum of x and y is even
coordinates = [(x, y) for x in range(3) for y in range(3) if (x + y) % 2 == 0]
print(f"Coordinates with even sum: {coordinates}")