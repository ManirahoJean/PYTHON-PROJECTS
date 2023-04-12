
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'black', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\n")

# use range() to create a fleet of 30 aliens
# Make an empty list for storing aliens.

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 lines

for alien in aliens[:5]:
    print(alien)

print("...\n")

# Show how many aliens have been created

print(f"Total number of aliens: {len(aliens)}\n")

# When it’s time to change colors, we can use a for loop and
# an if statement to change the color of aliens

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 lines

for alien in aliens[:5]:
    print(alien)
print("....")

print("\n")

# You could expand this loop by adding an elif block that turns yellow
# aliens into red, fast-moving ones worth 15 points each

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:10]:
    print(alien)
print("...")
