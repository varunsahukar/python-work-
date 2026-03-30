""" 
Topic 7: Error Handling 
====================== 
Covers: try, except, else, finally, raising exceptions, custom exceptions 
""" 

# ───────────────────────────────────────── 
# 1. Basic try-except 
# ───────────────────────────────────────── 
try: 
    number = int(input("Enter a number: ")) 
    result = 10 / number 
    print(f"Result: {result}") 
except ValueError: 
    print("Error: Please enter a valid integer.") 
except ZeroDivisionError: 
    print("Error: Cannot divide by zero.") 

# ───────────────────────────────────────── 
# 2. try-except-else-finally 
# ───────────────────────────────────────── 
try: 
    file = open("test.txt", "w") 
    file.write("Hello, World!") 
except IOError as e: 
    print(f"An error occurred: {e}") 
else: 
    print("File written successfully.") 
finally: 
    # This block always runs 
    if 'file' in locals() and not file.closed: 
        file.close() 
        print("File closed.") 

# ───────────────────────────────────────── 
# 3. Raising Exceptions 
# ───────────────────────────────────────── 
def check_age(age: int) -> None: 
    if age < 0: 
        raise ValueError("Age cannot be negative.") 
    print(f"Age is: {age}") 

try: 
    check_age(-5) 
except ValueError as e: 
    print(f"Caught an exception: {e}") 

# ───────────────────────────────────────── 
# 4. Custom Exceptions 
# ───────────────────────────────────────── 
class InsufficientFundsError(Exception): 
    """Exception raised for errors in the withdrawal process.""" 
    pass 

def withdraw(amount: float, balance: float) -> float: 
    if amount > balance: 
        raise InsufficientFundsError(f"Cannot withdraw {amount}, balance is {balance}.") 
    return balance - amount 

try: 
    new_balance = withdraw(100, 50) 
except InsufficientFundsError as e: 
    print(f"Error: {e}") 
