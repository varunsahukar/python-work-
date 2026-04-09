""" 
Topic 6: Object-Oriented Programming (OOP) 
========================================== 
Covers: class, init, self, methods, inheritance, super() 
""" 

# ───────────────────────────────────────── 
# 1. Basic Class Definition 
# ───────────────────────────────────────── 
class User: 
    def __init__(self, username: str, email: str): 
        self.username = username 
        self.email = email 

    def greet(self) -> str: 
        return f"Hello, I am {self.username}!" 

    # String representation (useful for debugging) 
    def __str__(self) -> str: 
        return f"User({self.username}, {self.email})" 

# Create instance 
user1 = User("arjun_codes", "arjun@example.com") 
print(user1.greet()) 
print(user1) 

# ───────────────────────────────────────── 
# 2. Inheritance 
# ───────────────────────────────────────── 
class Admin(User): 
    def __init__(self, username: str, email: str, access_level: int): 
        # super() calls the parent class constructor 
        super().__init__(username, email) 
        self.access_level = access_level 

    def delete_user(self, target_user: User) -> str: 
        return f"Admin {self.username} deleted {target_user.username}" 

admin1 = Admin("super_admin", "admin@site.com", 1) 
print(admin1.greet()) 
print(admin1.delete_user(user1)) 

# ───────────────────────────────────────── 
# 3. Encapsulation (Private attributes) 
# ───────────────────────────────────────── 
class BankAccount: 
    def __init__(self, owner: str, balance: float): 
        self.owner = owner 
        self.__balance = balance  # '__' makes it private 

    def deposit(self, amount: float): 
        if amount > 0: 
            self.__balance += amount 
            print(f"Deposited {amount}. New balance: {self.__balance}") 

    def get_balance(self) -> float: 
        return self.__balance 

account = BankAccount("Arjun", 1000) 
account.deposit(500) 
print(f"Final Balance: {account.get_balance()}") 
# print(account.__balance)  # ❌ Error: Attribute is private 
