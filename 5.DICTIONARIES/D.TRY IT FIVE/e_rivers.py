# 5.5 Rivers
rivers = {
    'nyabarongo': 'rwanda',
    'nile': 'egypt',
    'congo river': 'Republic democratic of congo'
}
for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}.")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nTheir respective countries: ")
for country in rivers.values():
    print(country.title())
