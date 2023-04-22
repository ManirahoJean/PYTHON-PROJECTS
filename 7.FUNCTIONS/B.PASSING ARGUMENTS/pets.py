# Positional Arguments

def describe_pet(animal_type, pet_name):
    """ Display information about pets"""
    print(f"\nI have a {animal_type}.")
    print(f"{animal_type}'s name is {pet_name}.")


describe_pet("hamster", "harry")

print("\n")

# Multiple Function Calls


def describe_pet(animal_type, pet_name):

    """ Display information about pets"""
    print(f"\nI have a {animal_type}.")
    print(f"{animal_type}'s name is {pet_name}.")


describe_pet("hamster", "harry")
describe_pet("dog", "willie")

# Order Matters in Positional Arguments
""" 
You can get unexpected results if you mix up the order of the arguments 
in a function call when using positional arguments
"""


def describe_pet(animal_type, pet_name):

    """ Display information about pets"""
    print(f"\nI have a {animal_type}.")
    print(f"{animal_type}'s name is {pet_name}.")


describe_pet("harry", "hamster")

print("\n")

# Keyword Arguments
"""A keyword argument is a name-value pair that you pass to a function"""


def describe_pet(animal_type, pet_name):

    """ Display information about pets"""
    print(f"\nI have a {animal_type}.")
    print(f"{animal_type}'s name is {pet_name}.")


describe_pet(animal_type="hamster", pet_name="harry")

print("\n")

# Default Values


def describe_pet(pet_name, animal_type='dog'):

    """ Display information about pets"""
    print(f"\nI have {animal_type}.")
    print(f"{animal_type}'s name is {pet_name}.")


describe_pet(pet_name='willie')

print("\ndone")

# Equivalent Function Calls


def describe_pet(pet_name, animal_type='dog'):

    """A dog named willie"""


describe_pet('willie')
describe_pet(pet_name='willie')

""" A hamster named harry """

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

""" Each of these function calls would have the same output as the previous 
examples """
