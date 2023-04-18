# 6.6 Three Exits
"""
6.6 Three Exits: Write different versions of either Exercise 6-4
or Exercise 6-5 that do each of the following at least once

Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit' value

"""
# 1. Use a conditional test in the while statement to stop the loop

prompt = "\nEnter your age: "
age = ""

while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        continue

    age = int(age)
    if age < 3:
        print("The ticket is free")
    elif age < 13:
        print("The ticket costs $ 10")
    else:
        print("The ticket costs $ 15")
        

# 2.Use an active variable to control how long the loop runs

prompt = "\nEnter your age: "
prompt += "\nEnter 'quit' to exit."

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False

    try:
        age = int(age)
        if age < 3:
            print("The ticket is free.")
        elif age < 13:
            print("The ticket is $10.")
        else:
            print("The ticket is $15")

    except ValueError:
        pass


# 3. Use a break statement to exit the loop when the user enters a 'quit' value

prompt = "\nEnter your age"
prompt += "\nEnter 'quit' to exit: "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("The ticket is free.")
    elif age < 13:
        print("The ticket costs $10.")
    else:
        print("The ticket is $15")






