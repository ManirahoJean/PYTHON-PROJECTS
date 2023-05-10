# 8-3. Users
"""
8-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""


class User:
    """ a simple attempt to model a user """
    def __init__(self, first_name, last_name, username, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.location = location.title()

    def describe_user(self):
        """Display a summary of user's information """
        print(f"First Name: {self.first_name}, Last Name: {self.last_name}")
        print(f"username: {self.username}")
        print(f"location: {self.location}")

    def greeter_user(self):
        print(f"Dear {self.first_name} {self.last_name}, you're most welcome!")


user = User('mani', 'jD', 'jadoma', 'kigali')
my_user = User('hategeka', 'kerrah', 'hatekerrah', 'huye')

user.describe_user()
user.greeter_user()
print(f"{user.first_name} {user.last_name} is living in {user.location}\n")

my_user.describe_user()
my_user.greeter_user()
print(f"{my_user.first_name} {my_user.last_name} is living in {my_user.location}")
