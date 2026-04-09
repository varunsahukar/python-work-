""" 
Topic 7: Error Handling 
======================= 
Covers: try, except, else, finally, custom exceptions 
""" 

# ───────────────────────────────────────── 
# 1. Basic Try/Except Block 
# ───────────────────────────────────────── 
try: 
    number = int(input("Enter a number to divide 100 by: ")) 
    result = 100 / number 
except ValueError: 
    print("❌ Error: You must enter a valid integer.") 
except ZeroDivisionError: 
    print("❌ Error: Cannot divide by zero.") 
else: 
    # Runs ONLY if no exception occurred 
    print(f"Success! Result: {result}") 
finally: 
    # Runs ALWAYS (e.g., closing a file or database connection) 
    print("Operation complete.") 

# ───────────────────────────────────────── 
# 2. Raising Exceptions 
# ───────────────────────────────────────── 
def set_age(age: int): 
    if age < 0: 
        raise ValueError("Age cannot be negative!") 
    print(f"Age set to: {age}") 

try: 
    set_age(-5) 
except ValueError as e: 
    print(f"Caught an error: {e}") 

# ───────────────────────────────────────── 
# 3. Custom Exceptions 
# ───────────────────────────────────────── 
class InsufficientFundsError(Exception): 
    """Raised when account balance is too low.""" 
    pass 

def withdraw(balance: float, amount: float): 
    if amount > balance: 
        raise InsufficientFundsError(f"Needed {amount}, but only have {balance}") 
    return balance - amount 

try: 
    withdraw(100, 250) 
except InsufficientFundsError as e: 
    print(f"Transaction failed: {e}") 
