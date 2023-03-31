# Simple conditional statement
cars = ['audi', 'subaru', 'bmw', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("\n")

# Checking for Equality

car = 'bmw'
print(car == 'bmw')  # it prints True
print(car == 'audi')  # it prints False

print("\n")

# Checking for Inequality

requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("hold the anchovies")

print("\n")

# Numerical Comparisons

age = 18
print(age == 18)  # it prints True

answer = 17
if answer != 42:
    print("That is not the correct answer, please try again!")

print("\n")

# Using and to Check Multiple Conditions

age_0 = 22
age_1 = 18
print((age_0 >= 21) and (age_1 >= 21))  # False, one of the conditions is false
age_1 = 22
print((age_0 >= 22) and (age_1 >= 22))  # True, both conditions are true

print("\n")

# Using or to Check Multiple Conditions

age_0 = 22
age_1 = 18
print((age_0 >= 21) or (age_1 >= 21))  # True, True if one of the conditions is true
age_0 = 18
print((age_0 >= 21) or (age_1 >= 21))  # False, false if both conditions fail

print("\n")

# Checking Whether a Value Is in a List

requested_topping_1 = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_topping_1)  # it prints yes
print('pepperoni' in requested_topping_1)

print("\n")

# Checking Whether a Value Is Not in a List

banned_users = ['david', 'charles', 'carolina']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish!")


