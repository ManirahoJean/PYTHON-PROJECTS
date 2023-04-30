# 7-9. Messages

"""
7-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message
"""


def show_messages(messages):
    """display short messages """
    print(f"\nMake her strong:")
    for message in messages:
        print(message)


messages = ['Here for her', 'He for she', 'she can', 'mighty woman']
show_messages(messages)
