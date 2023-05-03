# 7-14. Cars
"""
7-14. Cars: Write a function that stores information about a car in a
 dictionary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.

"""


def make_car(manufacturer_name, model_name, **other_features):
    """ Returning a dictionary containing everything about a car """
    other_features['manufacturer name'] = manufacturer_name
    other_features['model name'] = model_name
    return other_features


car = make_car('toyota', 'v6', color='black',
               tow_package=True)
print(car)

print("\nYou can also use this method:\n")


def make_car(manufacturer_name, model_name, **other_features):
    """ Returning a dictionary containing everything about a car"""
    car_dict = {
        'manufacturer name': manufacturer_name,
        'model name': model_name
    }

    """ Save the address in the dictionary """

    for option, value in other_features.items():
        car_dict[option] = value
    return car_dict


car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True,
               year=1995)
print(car)
