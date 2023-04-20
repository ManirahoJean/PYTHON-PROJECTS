# 6.8

sandwich_orders = ['pizza', 'peperoni', 'vegetables', 'meat', 'bread']
finished_sandwiches = []

# As each sandwich is made, move it to the list of finished sandwiches

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f"{current_sandwiches} sandwich is available to order")
    finished_sandwiches.append(current_sandwiches)

print("\nSandwiches that have been made:")

# Print the list of sandwiches that have been made

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
