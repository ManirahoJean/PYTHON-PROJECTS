# Returning a Simple Value

def get_formatted_name(first_name, last_name):

    """Return full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Argument Optional
"""
You can use default values to make an argument optional.
For example, say we want to expand get_formatted_name() to handle 
middle names as well
"""


def get_formatted_name(first_name, middle_name, last_name):

    """Return full name, neatly formatted"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician2 = get_formatted_name('mugisha', 'bana', 'emmanuel')
print(musician2)

print("\n")

# But middle names aren’t always needed
# To make the middle name optional, we can give the middle_name argument
# an empty default value


def get_formatted_name(first_name, last_name, middle_name=''):

    """Return full name, neatly formatted name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name} "
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('iga', 'justin')
print(musician)

musician = get_formatted_name('mbaraga', 'cyiza', 'goldmaker')
print(musician)
