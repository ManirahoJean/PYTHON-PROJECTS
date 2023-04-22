# 7-3. T-Shirt
"""
7-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""


# Call the function once using positional arguments to make a shirt
def make_shirt(size, message):

    """ Display the size and message"""
    print(f"Size: {size}, {message}")


make_shirt(34, '100% cotton')

print("\n")

# Call the function a second time using keyword arguments


def make_shirt(message, size=34):
    """ Display the size and message"""
    print(f"{size}, {message}")


make_shirt('98% cotton')

