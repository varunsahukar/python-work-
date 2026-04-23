""" 
Topic 9: Modules & Packages 
========================== 
Covers: import, from ... import, __init__.py, project structure 
""" 

# 1. Importing from a built-in module 
import math 
print(f"Square root of 16: {math.sqrt(16)}") 

# 2. Importing from our custom package 
from topic9_package import math_utils 

result_add = math_utils.add(10, 5) 
result_sub = math_utils.subtract(10, 5) 

print(f"Addition from package: {result_add}") 
print(f"Subtraction from package: {result_sub}") 

# 3. Importing specific functions 
from topic9_package.math_utils import add 
print(f"Direct function call: {add(20, 30)}") 
