# 6.2  Restaurant Seating

restaurant_seats = input("How many people are in your dinner group? ")
restaurant_seats = int(restaurant_seats)

if restaurant_seats > 8:
    print("You'll have to wait for a table")
else:
    print("your table is ready")
