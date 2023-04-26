# Using a Function with a while Loop
"""

def get_formatted_name(first_name, last_name):
    #Return full name, neatly formatted

    full_name = f"{first_name} {last_name}"
    return full_name

# This is an infinite loop


while True:
    print("\nPlease tell me our name.")
    f_name = input("Enter First Name: ")
    l_name = input("Enter Last Name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}")


# The only problem with this loop is that it has no quit condition
"""

# Define the quit condition


def get_formatted_name(first_name, last_name):

    """Return full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:

    print("\nTell me your name.")
    print("Enter 'q' any time to quit")

    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input(" Last Name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello {formatted_name}")
