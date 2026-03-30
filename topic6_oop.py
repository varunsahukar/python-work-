""" 
Topic 6: Object-Oriented Programming (OOP) 
========================================= 
Covers: Classes, objects, __init__, methods, inheritance, super() 
""" 

# ───────────────────────────────────────── 
# 1. Basic Class Definition 
# ───────────────────────────────────────── 
class Dog: 
    """A simple class representing a dog.""" 
     
    # Class attribute 
    species = "Canis familiaris" 

    def __init__(self, name: str, age: int): 
        """Initialize name and age attributes.""" 
        self.name = name 
        self.age = age 

    def bark(self) -> str: 
        """Return a barking sound.""" 
        return f"{self.name} says Woof!" 

    def __str__(self) -> str: 
        """Return a string representation of the object.""" 
        return f"{self.name} is {self.age} years old." 

# Creating objects (instances) 
my_dog = Dog("Buddy", 3) 
print(my_dog) 
print(my_dog.bark()) 
print(f"Species: {my_dog.species}") 

# ───────────────────────────────────────── 
# 2. Inheritance 
# ───────────────────────────────────────── 
class GoldenRetriever(Dog): 
    """A specialized class inheriting from Dog.""" 
     
    def fetch(self, item: str) -> str: 
        """Return a fetching message.""" 
        return f"{self.name} is fetching the {item}!" 

my_golden = GoldenRetriever("Goldie", 5) 
print(my_golden) 
print(my_golden.bark()) 
print(my_golden.fetch("ball")) 

# ───────────────────────────────────────── 
# 3. Using super() 
# ───────────────────────────────────────── 
class WorkingDog(Dog): 
    """A class for dogs that have jobs.""" 

    def __init__(self, name: str, age: int, job: str): 
        # Call the parent class __init__ 
        super().__init__(name, age) 
        self.job = job 

    def __str__(self) -> str: 
        return f"{super().__str__()} and works as a {self.job}." 

service_dog = WorkingDog("Max", 4, "Service Dog") 
print(service_dog) 
