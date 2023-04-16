# 6.3 Multiples of Ten

multiple_of_ten = input("Enter the number to check if is multiple of 10 or not: ")
multiple_of_ten = int(multiple_of_ten)

if multiple_of_ten % 10 == 0:
    print(f"{multiple_of_ten} is multiple of 10.")
else:
    print(f"{multiple_of_ten} is not multiple of 10")


