
cars = ['audi', 'subaru', 'bmw', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Checking for Inequality

requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("hold the anchovies")

# magic number

answer = 17
if answer != 42:
    print("That is not the correct answer, please try again!")

# Checking Whether a Value Is Not in a List

banned_users = ['david', 'charles', 'carolina']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish!")


