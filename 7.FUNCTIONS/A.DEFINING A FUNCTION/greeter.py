# functions are named blocks of code that are designed
# to do one specific job. When you want to perform a particular task
# that you’ve defined in a function, you call the function
# responsible for it

def greet_user():
    """ Display the message """
    print("Hello World!")


greet_user()

# Passing Information to a Function


def greet_user(username):

    """ Display greeting """
    print(f"Hello {username}.")


greet_user('jessie')

