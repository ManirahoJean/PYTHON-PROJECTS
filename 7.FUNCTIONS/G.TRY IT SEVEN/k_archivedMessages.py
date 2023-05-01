# 7-11. Archived Messages

"""
7-11. Archived Messages: Start with your work from Exercise 7-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
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
# send_messages(messages, sent_messages)
send_messages(messages[:], sent_messages)

print("\n final list: ")
print(messages)
print(sent_messages)
