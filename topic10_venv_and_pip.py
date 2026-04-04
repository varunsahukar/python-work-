""" 
Topic 10: Virtual Environments & pip 
=================================== 
Covers: venv, pip install, requirements.txt, .gitignore 
""" 

# This file serves as a guide for terminal commands related to environment management. 

# ───────────────────────────────────────── 
# 1. Creating a Virtual Environment 
# ───────────────────────────────────────── 
# Command: python -m venv venv 

# ───────────────────────────────────────── 
# 2. Activating the Environment 
# ───────────────────────────────────────── 
# Mac/Linux: source venv/bin/activate 
# Windows: venv\Scripts\activate 

# ───────────────────────────────────────── 
# 3. Installing Packages 
# ───────────────────────────────────────── 
# Command: pip install fastapi uvicorn requests 

# ───────────────────────────────────────── 
# 4. Generating requirements.txt 
# ───────────────────────────────────────── 
# Command: pip freeze > requirements.txt 

# ───────────────────────────────────────── 
# 5. Installing from requirements.txt 
# ───────────────────────────────────────── 
# Command: pip install -r requirements.txt 

def guide() -> None: 
    print("Check the comments in this file for environment management commands!") 

if __name__ == "__main__": 
    guide() 
