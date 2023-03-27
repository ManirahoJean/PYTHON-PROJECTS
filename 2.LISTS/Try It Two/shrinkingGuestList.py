# 2.7 Shrinking the list

guest_list = ['bwiza', 'bikori', 'kiza']

print(F"{guest_list[2]} will not make a dinner with us!")
guest_list[2] = 'kaje'

print("\nWe have found a bigger dinner table")
guest_list.insert(0, 'nzeyi')
guest_list.insert(1, 'hafasha')
guest_list.append('nzaba')

print(f"\n{guest_list[0].title()}, you're invited to our dinner!")
print(f"{guest_list[1].title()}, you're invited to our dinner!")
print(f"{guest_list[2].title()}, you're invited to our dinner!")
print(f"{guest_list[3].title()}, you're invited to our dinner!")
print(f"{guest_list[4].title()}, you're invited to our dinner!")

print("\nWe only have the place fo two people for dinner")
message = f"\n{guest_list.pop(-1).title()}, I'm sorry, you're not invited on the dinner"
print(message)

message = f"\n{guest_list.pop(4).title()}, I'm sorry, you're not invited on the dinner"
print(message)
print(f"{guest_list.pop(3).title()}, I'm sorry, you're not invited on the dinner")
print(f"{guest_list.pop(2).title()}, I'm sorry, you're not invited on the dinner")
del guest_list[1]
del guest_list[0]
print(guest_list)






