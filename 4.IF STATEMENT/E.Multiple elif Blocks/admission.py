age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 100_000
elif age < 65:
    price = 400_000
else:
    price = 200_00
print(f"Your admission cost is {price} Rwf")
