# 6.4 Pizza Toppings

# Using break

""""

prompt = "\nPlease enter the name of pizza you want"
prompt += "\nEnter 'quit' to end the program: "

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"You will {message.title()} topping to the pizza")

"""

# Using method of Setting a flag

prompt = "\nEnter the name of pizza you want"
prompt += "\nEnter 'quit' to end the program: "

active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"{message} topping will be added to your pizza")




