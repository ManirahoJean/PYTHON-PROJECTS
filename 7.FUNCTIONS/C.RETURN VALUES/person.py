# Returning a Dictionary


def build_person(first_name, last_name):

    """Return a dictionary"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('bwira', 'hunter')
print(musician)

# You can easily extend this function to accept
# optional values like a middle name, an age, an occupation,
# or any other information you want to store about a person


def build_person(first_name, last_name, age=None):

    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}

    if age:
        person['age'] = age
    return person


musician = build_person('kora', 'hustler', age=32)
print(musician)
