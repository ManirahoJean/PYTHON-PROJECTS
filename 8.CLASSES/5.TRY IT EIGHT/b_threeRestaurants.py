# 8-1. Restaurant

"""
8-2. Three Restaurants: Start with your class from Exercise 8-1. Create three
different instances from the class, and call describe_restaurant() for each
instance
"""


class Restaurant:
    """ A simple attempt to model a restaurant """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nIn {self.restaurant_name}, everyone is welcome!")
        print(f"{self.cuisine_type} is our foods")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")


restaurant = Restaurant('Happy Day', 'Traditional foods')
my_restaurant = Restaurant('health', 'modern food')
your_restaurant = Restaurant('live longer', 'tropical food')

print(f"\nOur restaurant's name is {restaurant.restaurant_name}")
print(f"Type of cuisine: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()

print(f"\nOur restaurant's name is {my_restaurant.restaurant_name}")
print(f"Type of cuisine: {my_restaurant.cuisine_type}.")
my_restaurant.describe_restaurant()

print(f"\nOur restaurant's name is {your_restaurant.restaurant_name}")
print(f"Type of cuisine: {your_restaurant.cuisine_type}.")
your_restaurant.describe_restaurant()

restaurant.open_restaurant()
