age = 12
if age < 4:
    print("Your admission cost is 0 Rwf")
elif age < 18:
    print("Your admission cost is 100,000 Rwf")
else:
    print("Your admission is 40, 000 Rwf cost")

print("\n")

# set the price inside the if-elif-else chain

age_1 = 12
if age_1 < 4:
    price = 0
elif age_1 < 18:
    price = 100_000
else:
    price = 40_000

print(f"Your admission is {price} Rwf cost")
