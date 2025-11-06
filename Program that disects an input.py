
text = input("Type in something: ")

print("\n--- Analysis ---")

print("Only white spaces:", text.isspace())
print("Only numbers:", text.isdigit())
print("Only alphabetical:", text.isalpha())
print("Alphanumeric:", text.isalnum())
print("All uppercase:", text.isupper())
print("All lowercase:", text.islower())
print("Title case (Capital case):", text.istitle())