""" 
Topic 5: Data Structures 
======================== 
Covers: list, tuple, dict, set, list comprehensions 
""" 

# ───────────────────────────────────────── 
# 1. Lists (Ordered, Mutable) 
# ───────────────────────────────────────── 
fruits: list[str] = ["apple", "banana", "cherry"] 
fruits.append("orange")      # Add to end 
fruits.insert(1, "mango")    # Add at index 
fruits.remove("banana")      # Remove by value 
popped = fruits.pop()        # Remove and return last item 

print(f"Fruits: {fruits}") 
print(f"Popped: {popped}") 

# List Comprehension (Clean & Pythonic) 
numbers = [1, 2, 3, 4, 5] 
squares = [n**2 for n in numbers if n > 2] 
print(f"Squares of n > 2: {squares}") 

# ───────────────────────────────────────── 
# 2. Tuples (Ordered, Immutable) 
# ───────────────────────────────────────── 
# Used for fixed data like coordinates 
point: tuple[int, int] = (10, 20) 
# point[0] = 15  # ❌ Error: Tuples cannot be changed 

# Unpacking 
x, y = point 
print(f"X: {x}, Y: {y}") 

# ───────────────────────────────────────── 
# 3. Dictionaries (Key-Value Pairs, Mutable) 
# ───────────────────────────────────────── 
user: dict[str, any] = { 
    "name": "Arjun", 
    "age": 25, 
    "is_student": True 
} 

print(f"Name: {user.get('name')}") 
user["email"] = "arjun@example.com"  # Add new key 

# Iterating 
for key, value in user.items(): 
    print(f"{key}: {value}") 

# ───────────────────────────────────────── 
# 4. Sets (Unordered, Unique elements) 
# ───────────────────────────────────────── 
tags: set[str] = {"python", "coding", "fastapi", "python"} 
print(f"Unique tags: {tags}")  # Only one 'python' 

tags.add("backend") 
print("fastapi" in tags)  # Fast membership check 
