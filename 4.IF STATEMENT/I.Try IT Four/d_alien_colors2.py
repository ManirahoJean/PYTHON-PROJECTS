# 4.4 alien color, one version that run if block and
# another that run else block

alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You earned 5 points by shooting the alien!")
else:
    print("You earned 5 points")

print("\n")

# run if block

if 'green' in alien_color:
    print("You earned 5 points")
else:
    print("You earned 10 points")

print("\n")

# block that runs else block

if 'white' in alien_color:
    print("You earned 5 points")
else:
    print("You just earned 10 points")
