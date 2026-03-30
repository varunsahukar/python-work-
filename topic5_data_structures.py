""" 
Topic 5: Data Structures 
======================= 
Covers: list, tuple, dict, set, list comprehensions 
""" 

# ───────────────────────────────────────── 
# 1. Lists (Ordered, Mutable) 
# ───────────────────────────────────────── 
fruits: list[str] = ["apple", "banana", "cherry"] 
fruits.append("orange") 
print(f"Fruits: {fruits}") 

# List Comprehension 
squared_numbers = [x**2 for x in range(1, 6)] 
print(f"Squared Numbers: {squared_numbers}") 

# ───────────────────────────────────────── 
# 2. Tuples (Ordered, Immutable) 
# ───────────────────────────────────────── 
coordinates: tuple[float, float] = (10.5, 20.3) 
print(f"Coordinates: {coordinates}") 
# coordinates[0] = 11.0  # This would raise a TypeError 

# ───────────────────────────────────────── 
# 3. Dictionaries (Key-Value Pairs, Mutable) 
# ───────────────────────────────────────── 
user: dict[str, str | int] = { 
    "name": "Arjun", 
    "age": 25, 
    "city": "Mumbai" 
} 
print(f"User Name: {user['name']}") 
user["role"] = "Developer" 
print(f"User Info: {user}") 

# ───────────────────────────────────────── 
# 4. Sets (Unordered, Unique elements) 
# ───────────────────────────────────────── 
unique_numbers: set[int] = {1, 2, 2, 3, 4, 4, 5} 
print(f"Unique Numbers: {unique_numbers}") # {1, 2, 3, 4, 5} 
unique_numbers.add(6) 
print(f"After adding 6: {unique_numbers}") 

# ───────────────────────────────────────── 
# 5. Common Operations 
# ───────────────────────────────────────── 
# Membership testing 
print(f"Is 'apple' in fruits? {'apple' in fruits}") 

# Length 
print(f"Number of fruits: {len(fruits)}") 
