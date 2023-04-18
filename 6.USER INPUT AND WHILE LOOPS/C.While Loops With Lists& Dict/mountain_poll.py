# Filling a Dictionary with User Input

responses = {}

# set a flag to indicate the polling is active

polling_active = True

while polling_active:

    # prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would like to climb first? ")

    # Store the responses in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete, show the result.

print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}?")















