"""
Now we’ll make a separate file called making_pizzas.py in the same
directory as pizza.py. This file imports the module we just created and then
makes two calls to make_pizza():

"""

import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green papers', 'extra cheers')

"""
If you use this kind of import statement to import 
an entire module named module_name.py, each function in the module is 
available through the following syntax:

module_name.function_name()
"""

# Importing Specific Functions
""" 
from module_name import function_name 
from module_name import function_name
from module_name import function_0, function_1, function_2

"""
print("\n")

from pizza import make_pizza
make_pizza(15, 'extra cheese')
make_pizza(20, 'green peppers', 'pepperoni', 'mushrooms')

print("\n")

# Using as to Give a Function an Alias

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


print("\n")

# Using as to Give a Module an Alias

import pizza as p

p.make_pizza(14, 'mushrooms')
p.make_pizza(12, 'extra cheese', 'pepperoni', 'green peppers')

print("\n")

# Importing All Functions in a Module

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
from module_name import *
"""