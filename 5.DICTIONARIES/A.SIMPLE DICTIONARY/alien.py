# A dictionary allows you to
# connect pieces of related information
# A dictionary in Python is a collection of key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Accessing Values in a Dictionary

print(alien_0['color'])

new_points = alien_0['points']
print(f"You just earned {new_points} points")

print("\n")

# Adding New Key-Value Pairs
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

print("\n")

# Starting with an Empty Dictionary

alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 25
print(alien_1)

# Modifying Values in a Dictionary

alien_2 = {'color': 'green'}
print(f"The alien is {alien_2['color']}")

alien_2['color'] = 'yellow'
print(f"The alien is now {alien_2['color']}.")

print("\n")

# let’s track the position of an alien that
# can move at different speeds

alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"The original position is : {alien_3['x_position']}")

print("\n")

# Move the alien to the right
# Determine how far to move the alien based on its current speed.

if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    # This must be the fast alien
    x_increment = 3
# The new position is the old position plus the increment

alien_3['x_position'] = alien_3['x_position'] + x_increment
print(f"New position is: {alien_3['x_position']}")

print("\n")

# Removing Key-Value Pairs

alien_4 = {'color': 'green', 'points': 25}
print(alien_4)

del alien_4['points']
print(alien_4)


