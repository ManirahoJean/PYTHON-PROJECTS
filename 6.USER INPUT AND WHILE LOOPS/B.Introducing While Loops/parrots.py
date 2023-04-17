# Letting the User Choose When to Quit

"""""
prompt = "\nTell me something,and I will repeat back to you"
prompt += "\nEnter 'quit' to end of the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    
"""""

# This program works well, except that it prints the word 'quit' as if it
# were an actual message. A simple if test fixes this:

"""""

prompt = "\nTell me something and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program: "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
        
"""""

# For a program that should run only as long as many conditions are true
# you can define one variable that determines whether or not the entire
# program is active. This variable, called a flag, acts as a signal to the program

prompt = "\nTell me something and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program: "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
