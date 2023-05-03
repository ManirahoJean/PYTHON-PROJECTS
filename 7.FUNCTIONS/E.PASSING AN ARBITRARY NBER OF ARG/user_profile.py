# Using Arbitrary Keyword Argument

"""
Sometimes you’ll want to accept an arbitrary number of arguments, but you
won’t know ahead of time what kind of information will be passed to the
function. In this case, you can write functions that accept as many key-value
pairs as the calling statement provides

"""


def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything we know about the user """
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

print("\n")

# using other way for making a profile dictionary


def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything about the user"""
    profile_dict = {
        'first name': first.title(),
        'last name': last.title()
    }

    for address, name in user_info.items():
        """ Save the address and name in the dictionary """
        profile_dict[address] = name
    return profile_dict


user_profile = build_profile('mani', 'jd',
                             location='kigali',
                             field='coding',
                             age=30)
print(user_profile)