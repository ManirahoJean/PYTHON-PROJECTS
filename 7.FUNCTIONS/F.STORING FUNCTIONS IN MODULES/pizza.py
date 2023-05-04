# Importing an Entire Module
"""
Let’s make a module that contains the function make_pizza(). To
make this module, we’ll remove everything from the file pizza.py except the
function make_pizza():

"""


def make_pizza(size, *toppings):
    """ Summarize pizza we're about to make """
    print(f"Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")
