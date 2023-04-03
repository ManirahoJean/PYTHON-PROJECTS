# 4.9 add if to make sure is not empty

usernames = ['jimmy', 'admin', 'john', 'olive', 'justine']

# let's make sure the list is not empty

if usernames:
    for user in usernames:
        print(f"Hello {user}, thank you for logging in")
else:
    print(f"We need to find new users")

print("\n")

# Remove all items to make sure the list is empty

usernames2 = []

if usernames2:
    for user2 in usernames2:
        print(f"Hello {user2}, thank you for logging in")
else:
    print("We need to find new users!")

# let remove all items through looping
# since we are not permitted to use for loop to remove all items from the list
# by using pop() method, we are going to use while loop

usernames3 = ['jimmy', 'admin', 'john', 'olive', 'justine']


print("\nUsers to be removed from our website: ")
while usernames3:
    for name3 in usernames3:
        print(name3)
        usernames3.pop()

print(usernames3)

# check if the list is empty and print "We need to find new users"

if usernames3:
    for user3 in usernames3:
        print(f"Hello {user3}, thank you for logging in")
else:
    print("We need to find new users")


