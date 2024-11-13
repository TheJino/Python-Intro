# Python Basics

# 1. Variables and Data Types
name = "Alice"            # String
age = 30                  # Integer
height = 5.7              # Float
is_student = False        # Boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# 2. Lists
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing list elements
print("First fruit:", fruits[0])

# Adding an item to the list
fruits.append("orange")
print("Updated Fruits:", fruits)

# 3. Dictionaries
person = {
    "name": "Bob",
    "age": 25,
    "is_student": True
}

print("Person:", person)

# Accessing dictionary values
print("Person's name:", person["name"])

# Adding a new key-value pair
person["height"] = 6.0
print("Updated Person:", person)

# 4. Functions
def greet(name):
    return f"Hello, {name}!"

# Function call
print(greet("Alice"))

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

print("Sum:", add_numbers(5, 3))

# 5. Conditionals
def check_age(age):
    if age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

print("Age category:", check_age(30))

# 6. Loops
# For loop
for i in range(5):
    print(f"Loop iteration {i}")

# While loop
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# 7. Classes
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())

# 8. File I/O
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a text file.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:", content)

# 9. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    print("This block always executes.")

# 10. List Comprehensions
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# 11. Lambda Functions
double = lambda x: x * 2
print("Double of 5:", double(5))
