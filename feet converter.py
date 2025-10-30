feet = float(input("enter the length in feet: "))

yards = feet / 3
miles = feet / 5280
inches = feet * 12
leagues = feet / 15840
meters = feet * 0.3048

print(f"{feet} feet is equal to {yards:.2f} yards. ")
print(f"{feet} feet is equal to {miles:.2f} miles. ")
print(f"{feet} feet is equal to {inches:.2f} inches. ")
print(f"{feet} feet is equal to {leagues:.2f} leagues. ")
print(f"{feet} feet is equal to {meters:.2f} meters. ")