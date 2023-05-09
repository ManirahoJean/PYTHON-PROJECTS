# Creating the Dog Class
"""
Each instance created from the Dog class will store a name and an age, and
we’ll give each dog the ability to sit() and roll_over():
"""


class Dog:
    """ A simple attempt to model a dog """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """ Simulate a dog sitting in response to a command. """
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """" Simulate rolling over in response to a command """
        print(f"{self.name} rolled over!")

# Making an Instance from a Class


my_dog = Dog('willie', 6)
print(f"my dog's name is {my_dog.name}.")
print(f"my dog's age is {my_dog.age} years old")


# Accessing Attributes
"""
To access the attributes of an instance, you use dot notation.
we access the value of my_dog’s attribute name by writing:

my_dog.name
"""

# Calling Methods

my_dog.sit()
my_dog.roll_over()

print("\n")

# Creating Multiple Instances

your_dog = Dog('lacy', 3)

print(f"my dog's name is {your_dog.name}")
print(f"my dog's age is {your_dog.age} years old")
your_dog.sit()
