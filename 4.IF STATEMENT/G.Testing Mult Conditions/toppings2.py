# The if-elif-else chain is powerful, but it’s only appropriate to use when you
# just need one test to pass
#  As soon as Python finds one test that passes, it
# skips the rest of the tests
# This behavior is beneficial, because it’s efficient
# and allows you to test for one specific condition

# However, sometimes it’s important to check all of the conditions of
# interest.

# In this case, you should use a series of simple if statements with no
# elif or else blocks


requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Add extra cheese")

print("Finished making your pizza")

print("\n")

# This code would not work properly if we used an if-elif-else block,
# because the code would stop running after only one test passes

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Add mushrooms")
elif 'pepperoni' in requested_toppings:
    print("Add pepperoni")
elif 'extra cheese' in requested_toppings:
    print("Add extra cheese")
print("Finished making your pizza")



