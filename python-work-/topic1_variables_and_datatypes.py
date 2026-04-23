""" 
Topic 1: Variables & Data Types 
================================ 
Covers: str, int, float, bool, None, type checking, 
        string methods, f-strings, ternary expressions 
""" 

def main():
    """Main function to demonstrate variables and data types."""
    # ─────────────────────────────────────────
    # 1. Basic variable assignment (snake_case always)
    # ─────────────────────────────────────────
    name: str = "Arjun"
    age: int = 25
    height: float = 5.9
    is_student: bool = True
    email = None  # NoneType

    # ─────────────────────────────────────────
    # 2. Type checking
    # ─────────────────────────────────────────
    print(type(name))       # <class 'str'>
    print(type(age))        # <class 'int'>
    print(type(height))     # <class 'float'>
    print(type(is_student)) # <class 'bool'>
    print(type(email))      # <class 'NoneType'>

    # ─────────────────────────────────────────
    # 3. String methods
    # ─────────────────────────────────────────
    raw_name = "  arjun  "

    print(raw_name.strip())       # "arjun"     → removes whitespace
    print(raw_name.strip().capitalize())  # "Arjun" → capitalize first letter
    print(name.upper())           # "ARJUN"
    print(name.lower())           # "arjun"
    print(name.replace("A", "@")) # "@rjun"
    print(len(name))              # 5
    print("Arjun" in name)        # True → membership check

    # ─────────────────────────────────────────
    # 4. f-strings (always use these — fastest & cleanest)
    # ─────────────────────────────────────────
    print(f"Hi, I'm {name}, {age} years old.")

    # Multi-line f-string
    profile = (
        f"Name   : {name}\n"
        f"Age    : {age}\n"
        f"Height : {height}\n"
        f"Student: {is_student}"
    )
    print(profile)

    # ─────────────────────────────────────────
    # 5. Ternary expression (inline if/else)
    # ─────────────────────────────────────────
    student_status = "a student" if is_student else "not a student"
    print(f"Hi, I'm {name}, {age} years old, and I am {student_status}.")

    # ─────────────────────────────────────────
    # 6. None check — always use 'is', never '=='
    # ─────────────────────────────────────────
    if email is None:
        print("No email provided.")

    if email is not None:
        print(f"Email: {email}")

    # ─────────────────────────────────────────
    # 7. Type conversion
    # ─────────────────────────────────────────
    age_str = str(age)        # int  → str
    age_back = int(age_str)   # str  → int
    pi = float("3.14")        # str  → float

    print(type(age_str))   # <class 'str'>
    print(type(age_back))  # <class 'int'>
    print(pi)              # 3.14

if __name__ == "__main__":
    main()