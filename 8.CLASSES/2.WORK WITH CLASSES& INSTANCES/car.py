# Working with Classes and Instances

"""
Our class will store information
about the kind of car we’re working with, and it will have a method that
summarizes this information
"""


class Car:
    """ A simple attempt to represent a car """
    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return neatly formatted descriptive name """
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

print("\n")

# Setting a Default Value for an Attribute
"""
Let’s add an attribute called odometer_reading that always starts with a 
value of 0. We’ll also add a method read_odometer() that helps us read each 
car’s odometer
"""


class Car:
    """ A simple attempt to represent a car """
    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return neatly formatted descriptive name """
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def read_odometer(self):
        """ Print a statement showing car's mileage """
        print(f"This car has {self.odometer_reading} miles on it")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying Attribute Values
"""
You can change an attribute’s value in three ways: you can change the value 
directly through an instance, set the value through a method, or increment 
the value (add a certain amount to it) through a method
"""

# Modifying an Attribute’s Value Directly
"""
The simplest way to modify the value of an attribute is to access 
the attribute directly through an instance
"""

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("\n")

# Modifying an Attribute’s Value Through a Method
"""
It can be helpful to have methods that update certain attributes for you. 
Instead of accessing the attribute directly, you pass the new value to a 
method that handles the updating internally
"""


class Car:
    """ A simple attempt to represent a car """
    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return neatly formatted descriptive name """
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def read_odometer(self):
        """ Print a statement showing car's mileage """
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """ Set the odometer reading to the given value """
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

my_new_car.update_odometer(24)
my_new_car.read_odometer()

print("\n")

"""
We can extend the method update_odometer() to do additional work 
every time the odometer reading is modified
"""


class Car:
    """ A simple attempt to represent a car """
    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return neatly formatted descriptive name """
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def read_odometer(self):
        """ Print a statement showing car's mileage """
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer reading")


my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(25)
my_new_car.read_odometer()

print("\n")

# Incrementing an Attribute’s Value Through a Method

"""
Sometimes you’ll want to increment an attribute’s value by a certain 
amount rather than set an entirely new value. Say we buy a used car and 
put 100 miles on it between the time we buy it and the time we register it
"""


class Car:
    """ A simple attempt to represent a car """
    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return neatly formatted descriptive name """
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def read_odometer(self):
        """ Print a statement showing car's mileage """
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer reading")

    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
