# 3.8  Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10)

for cubes in range(1, 11):
    print(cubes**3)

print("\n")

# This works too

cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)

for cube in cubes:
    print(cube)

print("\n")

#  print it as a list

cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)
print(cubes)
