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

def main():
    """Main function to demonstrate object-oriented programming."""
    # ─────────────────────────────────────────
    # 1. Basic Class Definition
    # ─────────────────────────────────────────
    # Create instance
    user1 = User("arjun_codes", "arjun@example.com")
    print(user1.greet())
    print(user1)

    # ─────────────────────────────────────────
    # 2. Inheritance
    # ─────────────────────────────────────────
    admin1 = Admin("super_admin", "admin@site.com", 1)
    print(admin1.greet())
    print(admin1.delete_user(user1))

    # ─────────────────────────────────────────
    # 3. Encapsulation (Private attributes)
    # ─────────────────────────────────────────
    account = BankAccount("Arjun", 1000)
    account.deposit(500)
    print(f"Final Balance: {account.get_balance()}")
    # print(account.__balance)  # ❌ Error: Attribute is private

if __name__ == "__main__":
    main()