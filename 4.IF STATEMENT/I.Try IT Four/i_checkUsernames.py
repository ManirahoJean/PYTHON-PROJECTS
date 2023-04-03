# 4.10 Do the following to create a program that simulates
# how websites ensure that everyone has a unique username

current_users = ['bwenge', 'koraneza', 'murava', 'byishimo', 'ngabo']
new_users = ['bwira', 'koraneza', 'mbaraga', 'mfura', 'NGABO']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is taken, please find another one")
    else:
        print(f"{new_user} is available")
