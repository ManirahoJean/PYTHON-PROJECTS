# 3.10 Make a copy of pizza

my_pizzas = ['cheese', 'meat', 'veggie', 'pepperoni']
my_friends_pizzas = my_pizzas[:]

my_pizzas.append('african pizza')
my_friends_pizzas.append('vegetable pizza')

print("my favorite pizza are :\n")

for pizza in my_pizzas:
    print(pizza)

print("\n")

print("my friend's favorite pizzas are :\n")

for pizzas in my_friends_pizzas:
    print(pizzas)
