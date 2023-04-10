# Using get() to Access Values

alien_5 = {'color': 'green', 'speed': 'slow'}

# print(alien_5['points']) This results in a traceback, showing a KeyError
# point value does not exist

# you can use the get() method to
# set a default value that will be returned if the requested key does not exist

point_value = alien_5.get('points', 'No point available')
print(point_value)



