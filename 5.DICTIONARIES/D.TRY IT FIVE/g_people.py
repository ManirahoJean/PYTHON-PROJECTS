# 5.7 People
# Display all the information in the dictionary

# first_person= {'first_name': 'Vincent', 'last_name': 'kira', 'age': 30, 'city': 'kigali'}
# second_person = {'first_name': 'Kenny', 'lsat_name': 'nziza', 'age': 25, 'city': 'Huye'}
# third_person = {'fist_name': 'Remgy', 'last_name': 'kora', 'age': 35, 'city': 'musanze'}


people = {
    'first_person': {
        'first_name': 'Vincent',
        'last_name': 'kira',
        'age': 30,
        'city': 'kigali'
    },
    'second_person': {
        'first_name': 'Kenny',
        'last_name': 'nziza',
        'age': 25,
        'city': 'Huye'
    },
    'third_person': {
        'first_name': 'Remgy',
        'last_name': 'kora',
        'age': 35,
        'city': 'musanze'
    }
}

for name, identity in people.items():
    print(f"Welcome {identity['first_name'].title()}  {identity['last_name'].title()}")
    print("Identity")
    print(f"\tAge:{identity['age']}years old,  City: {identity['city'].title()}\n")
