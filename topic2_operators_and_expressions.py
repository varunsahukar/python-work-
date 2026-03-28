""" 
Topic 2: Operators & Expressions 
================================== 
Covers: arithmetic, comparison, logical, assignment 
        shortcuts, identity, membership operators 
""" 

# ───────────────────────────────────────── 
# 1. Arithmetic operators 
# ───────────────────────────────────────── 
a: float = 15 
b: float = 4 

print(f"{a} + {b}  = {a + b}")   # 19   → addition 
print(f"{a} - {b}  = {a - b}")   # 11   → subtraction 
print(f"{a} * {b}  = {a * b}")   # 60   → multiplication 
print(f"{a} ** {b} = {a ** b}")  # 50625 → power 
print(f"{a} / {b}  = {a / b}")   # 3.75 → division (always float) 
print(f"{a} // {b} = {a // b}")  # 3    → floor division (drops decimal) 
print(f"{a} % {b}  = {a % b}")   # 3    → modulus (remainder) 

# ───────────────────────────────────────── 
# 2. Comparison operators (return True/False) 
# ───────────────────────────────────────── 
print(f"{a} > {b}  → {a > b}")   # True 
print(f"{a} < {b}  → {a < b}")   # False 
print(f"{a} == {b} → {a == b}")  # False 
print(f"{a} != {b} → {a != b}")  # True 
print(f"{a} >= 15  → {a >= 15}") # True 
print(f"{a} <= 10  → {a <= 10}") # False 

# ───────────────────────────────────────── 
# 3. Logical operators 
# ───────────────────────────────────────── 
print(True and False)  # False → both must be True 
print(True or False)   # True  → at least one must be True 
print(not True)        # False → flips the value 

# Real-world example 
is_adult: bool = a >= 18 
is_valid: bool = a is not None 

print(f"Is a valid and greater? {a > b and a is not None}") 

# ───────────────────────────────────────── 
# 4. Assignment shortcuts 
# ───────────────────────────────────────── 
x: int = 10 
x += 5    # x = x + 5  → 15 
x -= 3    # x = x - 3  → 12 
x *= 2    # x = x * 2  → 24 
x //= 5   # x = x // 5 → 4 
x **= 2   # x = x ** 2 → 16 
print(f"x after all shortcuts: {x}")  # 16 

# ───────────────────────────────────────── 
# 5. Identity operators — use for None checks 
# ───────────────────────────────────────── 
value = None 

print(value is None)      # True  ✅ correct way to check None 
print(value is not None)  # False 

# ───────────────────────────────────────── 
# 6. Membership operators 
# ───────────────────────────────────────── 
fruits: list = ["apple", "mango", "banana"] 

print("mango" in fruits)       # True 
print("grape" not in fruits)   # True 
print("apple" in fruits)       # True 

# ───────────────────────────────────────── 
# 7. Operator precedence (PEMDAS) 
# ───────────────────────────────────────── 
result = 2 + 3 * 4      # 14 → multiplication first 
result_with_parens = (2 + 3) * 4  # 20 → parens first 

print(f"Without parens : {result}")            # 14 
print(f"With parens    : {result_with_parens}") # 20
