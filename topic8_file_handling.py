""" 
Topic 8: File Handling 
====================== 
Covers: open(), read(), write(), append(), context managers (with), JSON 
""" 
import json 
import os 

# ───────────────────────────────────────── 
# 1. Basic File Writing 
# ───────────────────────────────────────── 
# Using a context manager ensures the file is closed automatically 
with open("example.txt", "w") as file: 
    file.write("Hello, this is a test file.\n") 
    file.write("Writing multiple lines is easy.\n") 

print("File 'example.txt' created.") 

# ───────────────────────────────────────── 
# 2. Reading from a File 
# ───────────────────────────────────────── 
print("\nReading entire file:") 
with open("example.txt", "r") as file: 
    content = file.read() 
    print(content) 

print("Reading line by line:") 
with open("example.txt", "r") as file: 
    for line in file: 
        print(f"Line: {line.strip()}") 

# ───────────────────────────────────────── 
# 3. Appending to a File 
# ───────────────────────────────────────── 
with open("example.txt", "a") as file: 
    file.write("This line was appended later.\n") 

print("\nAfter appending:") 
with open("example.txt", "r") as file: 
    print(file.read()) 

# ───────────────────────────────────────── 
# 4. JSON Handling 
# ───────────────────────────────────────── 
user_data = { 
    "name": "Arjun", 
    "skills": ["Python", "FastAPI", "PostgreSQL"], 
    "is_active": True 
} 

# Writing JSON 
with open("data.json", "w") as json_file: 
    json.dump(user_data, json_file, indent=4) 

print("\nJSON file 'data.json' created.") 

# Reading JSON 
with open("data.json", "r") as json_file: 
    loaded_data = json.load(json_file) 
    print(f"Loaded JSON Data: {loaded_data}") 
    print(f"User Name: {loaded_data['name']}") 
