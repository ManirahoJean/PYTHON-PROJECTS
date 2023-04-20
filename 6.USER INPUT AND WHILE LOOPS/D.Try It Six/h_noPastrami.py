#  Using the list sandwich_orders from Exercise 6-8, make sure
# the sandwich 'pastrami' appears in the list at least three times

sandwich_orders = ['pizza', 'pastrami', 'peperoni', 'pastrami', 'vegetables', 'meat', 'pastrami']
finished_sandwiches = []

print("deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f"I' working on {current_sandwiches} ")
    finished_sandwiches.append(current_sandwiches)

print("\nFinished Sandwiches:")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
