# 6.10 Dream Vacation

"""
Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.

"""


name_prompt = "\nEnter your name: "
place_prompt = "\nWhat is favorite place  would you visit? "
otherPlace_prompt = "\nWould you like to recommend other else?(yes/no) "
responses = {}

# Input the prompt

while True:

    name = input(name_prompt)
    place = input(place_prompt)
    repeat = input(otherPlace_prompt)

    # store responses in the dictionary

    responses[name] = place
    if repeat == 'no':
        break

print("\n---Dream Vacation---")

for name, place in responses.items():
    print(f"{name.title()} would like to visit {place} city.")


# Using method of setting Flag

name_prompt = "\nEnter your name: "
place_prompt = "\nWhat is your favorite place to visit? "
otherPlace_prompt = "\nWould you like to recommend other? "

responses = {}

vacation_active = True

while vacation_active:

    # Input prompt
    name = input(name_prompt)
    place = input(place_prompt)
    repeat = input(otherPlace_prompt)

    # Store the responses in dictionary
    responses[name] = place

    if repeat == 'no':
        vacation_active = False

# polling is complete, show the results

print("\n---Dream Vacation---")

for name, place in responses.items():
    print(f"{name} is visiting {place} city")
