# Tuples refers to the values that cannot be changed
#  and an immutable list is called a tuple.

dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 300 this is the error

print(dimensions)

# Looping Through All Values in a Tuple

print("\nOriginal dimensions are: \n")

for dimension in dimensions:
    print(dimension)


dimensions = (400, 200)

print("\nModified dimensions are: \n")

for dimension in dimensions:
    print(dimension)
