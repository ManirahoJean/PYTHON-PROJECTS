# 4.11 Ordinal numbers

ordinalNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for ordinalNum in ordinalNumbers:
    if ordinalNum == 1:
        print(f"{ordinalNum}st")
    elif ordinalNum == 2:
        print(f"{ordinalNum}nd")
    elif ordinalNum == 3:
        print(f"{ordinalNum}rd")
    else:
        print(F"{ordinalNum}th")
