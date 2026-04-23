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

def main():
    """Main function to demonstrate functions."""
    # ─────────────────────────────────────────
    # 1. Basic Function with Type Hints
    # ─────────────────────────────────────────
    message = greet("Arjun")
    print(message)

    # ─────────────────────────────────────────
    # 2. Function with Default Parameters
    # ─────────────────────────────────────────
    print(power(3))    # 3^2 = 9
    print(power(3, 3)) # 3^3 = 27

    # ─────────────────────────────────────────
    # 3. Variable Arguments (*args)
    # ─────────────────────────────────────────
    print(sum_all(1, 2, 3, 4, 5)) # 15

    # ─────────────────────────────────────────
    # 4. Keyword Arguments (**kwargs)
    # ─────────────────────────────────────────
    print_user_info(name="Arjun", city="Mumbai", role="Developer")

    # ─────────────────────────────────────────
    # 5. Functions as First-Class Citizens
    # ─────────────────────────────────────────
    print(apply_op(10, 5, multiply)) # 50

    # ─────────────────────────────────────────
    # 6. Lambda Functions (Short Anonymous Functions)
    # ─────────────────────────────────────────
    add = lambda x, y: x + y
    print(add(10, 20)) # 30

    # Often used with sorted(), map(), or filter()
    names = ["Arjun", "Zoe", "Bob", "Alice"]
    sorted_names = sorted(names, key=lambda name: len(name))
    print(f"Sorted by length: {sorted_names}")

    # ─────────────────────────────────────────
    # 7. Scope (Global vs Local)
    # ─────────────────────────────────────────
    increment()
    increment()
    print(f"Final global count: {count}")

if __name__ == "__main__":
    main()