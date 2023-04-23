# 7-4. Large Shirts

"""
7-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""


def make_shirt(size='Large', message='I love Python'):

    """ Display the size and message"""
    print(f"Size: {size}, Message: {message}")


make_shirt()

print("\n")


def make_shirt(size='Medium', message='I love python'):

    """Display information"""
    print(f"size: {size}.")
    print(f"Message: {message}.")


make_shirt()

print("\n")


def make_shirt(size='Small size', message='I love coding'):

    """Display size and message"""
    print(f"size: {size}.")
    print(f"Message: {message}.")
    print("Thank you!")


make_shirt()
