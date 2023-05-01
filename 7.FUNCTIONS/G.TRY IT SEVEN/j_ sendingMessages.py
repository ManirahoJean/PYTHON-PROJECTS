# 7-10. Sending Messages

"""
7-10. Sending Messages: Start with a copy of your program from Exercise 7-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly
"""


def show_messages(messages):
    """show all messages"""

    print("Messages to send: ")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Display messages that have been sent"""

    print(f"\nSent messages :")
    while messages:

        current_messages = messages.pop()
        print(current_messages)
        sent_messages.append(current_messages)


messages = ['we are here for her', 'He for she', 'she can', 'mighty woman']
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)