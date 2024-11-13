# basic_structure.py

# 1. Variables and Data Types
# ---------------------------
# Variables store data that can be used later in the code.

# Integer
age = 25

# Float
height = 5.9

# String
name = "John Doe"

# Boolean
is_student = True

# List (Array)
fruits = ["apple", "banana", "cherry"]

# Dictionary (Map)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# 2. Conditional Statements
# --------------------------
# Conditional statements allow you to make decisions in your code.

if age > 18:
    print("You are an adult.")
elif age == 18:
    print("You just turned an adult!")
else:
    print("You are a minor.")

# 3. Loops
# --------
# Loops allow you to repeat a block of code multiple times.

# For Loop (iterates over a sequence)
for fruit in fruits:
    print(fruit)

# While Loop (repeats as long as a condition is true)
count = 0
while count < 5:
    print("Counting...", count)
    count += 1

# 4. Functions
# ------------
# Functions allow you to group code into reusable blocks.

def greet(name):
    """
    This function greets a person with their name.
    """
    return f"Hello, {name}!"

# Using the function
print(greet("Alice"))

# 5. Input/Output
# ---------------
# Getting input from the user and displaying output.

# Getting user input
user_name = input("Enter your name: ")

# Displaying output
print(f"Welcome, {user_name}!")

# 6. Exception Handling
# ---------------------
# Handling errors that might occur during code execution.

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")

# 7. Classes and Objects
# ----------------------
# Object-oriented programming allows you to model real-world entities.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

# Creating an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Using the object's method
print(my_dog.bark())
