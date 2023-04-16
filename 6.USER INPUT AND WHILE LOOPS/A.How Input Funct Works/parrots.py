# The input() function pauses your program and waits for the user to enter
# some text

"""""
message = input("Tell me something, I will repeat it back to you: ")
print(message)

"""""
# Writing Clear Prompts

"""""
name = input("Please enter your name: ")
print(f"\nHello {name.title()}!")

"""""

# Sometimes you’ll want to write a prompt that’s longer than one line

prompt = "If You tell us who you are, we can personalize the message you see"
prompt += "What is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# When you use the input() function, Python interprets everything the user
# enters as a string





