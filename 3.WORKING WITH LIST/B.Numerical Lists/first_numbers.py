# Using the range() Function
# range print 1 to 4

for value in range(1, 5):
    print(value)

print("\n")

# Using range() to Make a List of Numbers

numbers = list(range(1, 6))
print(numbers)

print("\n")

# use the range() function to tell Python to skip numbers in a
# given range

# the range starts by 2, add 2 repeatedly until it reaches the last value

even_number = list(range(2, 11, 2))
print(even_number)

print("\n")

# a list of the first 10 square numbers

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

print("\n")

# writing codes more concisely

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

print("\n")

# Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print("\n")

# List Comprehensions
# combines the for loop and the creation of new elements into one line

squares = [value**2 for value in range(1, 11)]
print(squares)



