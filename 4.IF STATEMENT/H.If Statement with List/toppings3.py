# Checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Add {requested_topping}.")
print("Finished making your pizza")

print("\n")

# But what if the pizzeria runs out of green peppers?

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are running out of green peppers")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!")
