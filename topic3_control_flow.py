""" 
Topic 3: Control Flow 
===================== 
Covers: if/elif/else, for loops, while loops, 
        break, continue, match (Python 3.10+) 
""" 

# ───────────────────────────────────────── 
# 1. Conditionals (if, elif, else) 
# ───────────────────────────────────────── 
age: int = 20 

if age < 13: 
    print("Child") 
elif age < 20: 
    print("Teenager") 
else: 
    print("Adult") 

# ───────────────────────────────────────── 
# 2. Match Statement (Python 3.10+) 
# ───────────────────────────────────────── 
# Clean alternative to multiple if/elif for specific values 
status_code: int = 404 

match status_code: 
    case 200: 
        print("Success") 
    case 404: 
        print("Not Found") 
    case 500: 
        print("Server Error") 
    case _: 
        print("Unknown Status") 

# ───────────────────────────────────────── 
# 3. For Loops (iterating over sequences) 
# ───────────────────────────────────────── 
fruits: list[str] = ["apple", "banana", "cherry"] 

# Basic for loop 
for fruit in fruits: 
    print(f"I like {fruit}") 

# For loop with range() 
for i in range(5):  # 0 to 4 
    print(f"Number: {i}") 

# For loop with enumerate() — get both index and value 
for index, fruit in enumerate(fruits): 
    print(f"Fruit {index + 1}: {fruit}") 

# ───────────────────────────────────────── 
# 4. While Loops 
# ───────────────────────────────────────── 
count: int = 0 
while count < 3: 
    print(f"Counting: {count}") 
    count += 1 

# ───────────────────────────────────────── 
# 5. Loop Control: break and continue 
# ───────────────────────────────────────── 
print("\nTesting break and continue:") 

# break: exit the loop immediately 
for i in range(10): 
    if i == 5: 
        print("Breaking at 5") 
        break 
    print(i, end=" ") 

print() 

# continue: skip the rest of the current iteration 
for i in range(5): 
    if i == 2: 
        print("Skipping 2") 
        continue 
    print(f"Processing {i}") 

# ───────────────────────────────────────── 
# 6. For-Else (Rarely used but good to know) 
# ───────────────────────────────────────── 
# The 'else' block runs only if the loop finishes naturally (no 'break') 
search_for: str = "mango" 
for fruit in fruits: 
    if fruit == search_for: 
        print(f"Found {search_for}!") 
        break 
else: 
    print(f"Could not find {search_for} in the list.") 
