# 5.6 Favorite languages

favorite_languages = {
    'jane': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
workers = ['eddie', 'eric', 'jane', 'phil', 'emmy']

print("\nPeople who should take favorite languages poll!:\n")
for name in favorite_languages.keys():
    print(name.title())

print("\n")

# Loop through the list
#  If they have
# already taken the poll, print a message thanking them for responding
# If they have not yet taken the poll, print a message inviting them to take
# the poll.


for name in favorite_languages.keys():
    if name in workers:
        print(f"{name.title()}, Thank you for responding")
    else:
        print(f"{name.title()}, We invite you to the poll!")
