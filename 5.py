# Record (using Python class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance
person = Person("Rakib", 22)

# Accessing fields
print(f"Name: {person.name}, Age: {person.age}")
