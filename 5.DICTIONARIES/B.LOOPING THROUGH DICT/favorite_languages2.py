
favorite_languages = {
    'jane': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

# Looping Through All the Keys in a Dictionary

for name in favorite_languages.keys():
    print(name.title())

print("\n")

# Checking if name matches one of our friends
favorite_languages = {
    'jane': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language1 = favorite_languages[name].title()
        print(f"\t{name}, I see you love {language1}")

print("\n")

# You can also use the keys() method to find out if a particular person
# was polled

if 'erin' not in favorite_languages.keys():
    print("Erin, please make our poll!")

print("\n")

# Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages = {
    'jane': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in sorted(favorite_languages.keys()):
    print(f"{name}, Thank you for taking our poll!")

# Looping Through All Values in a Dictionary
# This approach pulls all the values from the dictionary without checking
# for repeats

print("\nThe following languages have been mentioned:")
for language2 in favorite_languages.values():
    print(language2.title())

print("\n")

# To see each language chosen without repetition, we can use a set.
# A set is a collection in which each item must be unique:

print("The following languages have been mentioned")
for language in set(favorite_languages.values()):
    print(language)




