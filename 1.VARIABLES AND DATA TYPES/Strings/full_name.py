# These strings are called f-strings

first_name = "python"
last_name = "language"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello,{first_name} {last_name}!")

message = f"Hello, {full_name.title()}!"
print(message)

#  format() method
# Each variable is referred to by a set of braces

full_name = "{} {}".format(first_name, last_name)
print(full_name)

# Adding Whitespace to Strings with Tabs or Newlines
# To add tab use \t

print("\tpython")

# To add new line use \n
print("My Languages: \nPython\nJavascript")
print("My Languages: \n\tPython\n\tJavascript")

# Stripping Whitespace
# To ensure that no whitespace exists at the right end of a string, use
# the rstrip() method.

favorite_animal = 'zebra '  # white space at right side
favorite_animal.rstrip()    # removing the white space right side or
favorite_animal = favorite_animal.rstrip()

# Strip white space from left

favorite_foods = ' fruits'  # white at left side
favorite_foods.lstrip()     # removing white space

# Avoiding Syntax Errors with Strings
# python can't identify where string ends, the following is error
"""
msm = 'One of Python's strengths is its diverse community.'

"""























