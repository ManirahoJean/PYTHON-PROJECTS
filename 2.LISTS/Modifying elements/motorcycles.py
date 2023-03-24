# Modifying element in a list

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding element in a list
# 1. Appending element in a list

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('suzuki')
motorcycles.append('yamaha')
motorcycles.append('honda')
print(motorcycles)

# inserting element in a list
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing an element from a list

del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was {last_owned.title()}!")

# Popping Items from any Position in a List

shoes = ['nike', 'adidas', 'timba']
first_owned = shoes.pop(1)
print(f"The first shoes I owned was {first_owned.title()}!")
shoes.append("adidas")

# Removing an Item by Value

shoes.remove("timba")
print(shoes)
too_expensive = 'nike'
print(f"\nA {too_expensive} is expensive for me ")

















