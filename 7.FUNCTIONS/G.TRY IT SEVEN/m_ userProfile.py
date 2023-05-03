# 7-13. User Profile:
"""
7-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you
"""


def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything about me"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


build_info = build_profile('Mani', 'JD',
                           location='Kigali',
                           field='coding',
                           status='single')
print(build_info)
