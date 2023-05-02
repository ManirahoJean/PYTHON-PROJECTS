"""
Sometimes you won’t know ahead of time how many arguments a function
needs to accept. Fortunately, Python allows a function to collect an
arbitrary number of arguments from the calling statement
"""


def make_pizza(*toppings):
    """ Print all toppings that have been requested"""
    print(toppings)


make_pizza('peperoni')
make_pizza('peperoni', 'sandwich', 'vegetable pizza')

"""
Now we can replace the print() call with a loop that runs through the 
list of toppings and describes the pizza being ordered:
"""
print("\n")


def make_pizza(*toppings):
    """ Print all toppings that have been requested """
    print("\nMaking pizza with the following toppings: ")
    for topping in toppings:
        print(topping)


make_pizza('peperoni')
make_pizza('sandwich', 'vegetable pizza', 'peperoni')

# Mixing Positional and Arbitrary Arguments

"""
If you want a function to accept several different kinds of arguments, the 
parameter that accepts an arbitrary number of arguments must be placed 
last in the function definition. Python matches positional and keyword 
arguments first and then collects any remaining arguments in the final 
parameter

"""


def make_pizza(size, *toppings):
    """ Summarise the pizza we're about to make """
    print(f"\nMaking {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'peperoni')
make_pizza(14, 'vegetable pizza', 'sandwich', 'peperoni')
