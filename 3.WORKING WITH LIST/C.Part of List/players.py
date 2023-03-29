# Slicing a List

players = ['gatete', 'sungura', 'mangwende', 'gaju', 'murisa']

print(players[0:3])
print(players[0:4])
print(players[:3])  # python automatically starts slicing at the beginning of the list
print(players[2:])  # python returns all items from the third
print(players[-3:])  # output the last three players

# Looping Through a Slice

players = ['gatete', 'sungura', 'mangwende', 'gaju', 'murisa']

print("In my team, those are my three players\n")
for player in players[:3]:
    print(player.title())

# Copying a list

my_favorite_foods = ['vegetables', 'fruits', 'meat pizza']
friends_favorite_foods = my_favorite_foods[:]  # make a copy

print("\nMy favorite foods are:")
print(my_favorite_foods)

print("\nMy friend's favorite foods are :")
print(friends_favorite_foods)

my_favorite_foods.append('African meat')
friends_favorite_foods.append('ice cream')

print(my_favorite_foods)
print(friends_favorite_foods)













