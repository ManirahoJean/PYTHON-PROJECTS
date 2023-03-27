# 2.6 inviting more people

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



