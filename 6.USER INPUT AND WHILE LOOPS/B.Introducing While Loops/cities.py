# Using break to Exit a Loop

# To exit a while loop immediately without running any remaining code in the
# loop, regardless of the results of any conditional test, use the break statement.
# The break statement directs the flow of your program; you can use it
# to control which lines of code are executed and which aren’t, so the program only
# executes code that you want it to, when you want it to

prompt = "\nPlease enter the name of the city you visited!"
prompt += "\nEnter 'quit' when you're finished: "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I would like to go to {city.title()}")
