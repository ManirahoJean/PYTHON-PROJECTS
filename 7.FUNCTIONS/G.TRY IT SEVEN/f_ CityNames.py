# 7.6  City Names

"""
7-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
"""


def city_country(city, country):

    """Return address of a country"""
    full_address = f"{city}, {country}"
    return full_address.title()


my_country = city_country('kigali', 'rwanda')
print(my_country)

my_country = city_country('kampala', 'uganda')
print(my_country)

my_country = city_country('bujumbura', 'burundi')
print(my_country)

