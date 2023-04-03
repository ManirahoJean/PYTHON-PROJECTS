# 4.8 list of five or more usernames
usernames = ['jimmy', 'admin', 'john', 'olive', 'justine']
for name in usernames:
    if name == 'admin':
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in")
