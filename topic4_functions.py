""" 
Topic 4: Functions 
================== 
Covers: def, return, type hints, default params, 
        *args, **kwargs, docstrings, lambdas 
""" 

# ───────────────────────────────────────── 
# 1. Basic Function with Type Hints 
# ───────────────────────────────────────── 
def greet(name: str) -> str: 
    """Returns a personalized greeting.""" 
    return f"Hello, {name}!" 

message = greet("Arjun") 
print(message) 

# ───────────────────────────────────────── 
# 2. Function with Default Parameters 
# ───────────────────────────────────────── 
def power(base: int, exponent: int = 2) -> int: 
    """Calculates base raised to the exponent (default: square).""" 
    return base ** exponent 

print(power(3))    # 3^2 = 9 
print(power(3, 3)) # 3^3 = 27 

# ───────────────────────────────────────── 
# 3. Variable Arguments (*args) 
# ───────────────────────────────────────── 
def sum_all(*numbers: float) -> float: 
    """Returns the sum of any number of numerical inputs.""" 
    return sum(numbers) 

print(sum_all(1, 2, 3, 4, 5)) # 15 

# ───────────────────────────────────────── 
# 4. Keyword Arguments (**kwargs) 
# ───────────────────────────────────────── 
def print_user_info(**info: str) -> None: 
    """Prints arbitrary key-value pairs representing user data.""" 
    for key, value in info.items(): 
        print(f"{key.capitalize()}: {value}") 

print_user_info(name="Arjun", city="Mumbai", role="Developer") 

# ───────────────────────────────────────── 
# 5. Functions as First-Class Citizens 
# ───────────────────────────────────────── 
def apply_op(a: int, b: int, operation) -> int: 
    """Applies a passed-in function (operation) to two numbers.""" 
    return operation(a, b) 

def multiply(x: int, y: int) -> int: 
    return x * y 

print(apply_op(10, 5, multiply)) # 50 

# ───────────────────────────────────────── 
# 6. Lambda Functions (Short Anonymous Functions) 
# ───────────────────────────────────────── 
# syntax: lambda arguments: expression 
add = lambda x, y: x + y 
print(add(10, 20)) # 30 

# Often used with sorted(), map(), or filter() 
names = ["Arjun", "Zoe", "Bob", "Alice"] 
sorted_names = sorted(names, key=lambda name: len(name)) 
print(f"Sorted by length: {sorted_names}") 

# ───────────────────────────────────────── 
# 7. Scope (Global vs Local) 
# ───────────────────────────────────────── 
count = 0  # Global variable 

def increment() -> None: 
    global count 
    count += 1 
    print(f"Internal count: {count}") 

increment() 
increment() 
print(f"Final global count: {count}") 
