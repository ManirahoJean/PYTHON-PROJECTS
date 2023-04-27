# Passing A List

# You’ll often find it useful to pass a list to a function, whether
# it’s a list of  names, numbers, or more complex objects, such as dictionaries

def greet_users(names):
    """Print a simple greeting to each user in te list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['emmy', 'nicky', 'jd']

greet_users(usernames)
