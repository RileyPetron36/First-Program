a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))


if b == 0:
    print("Error: Division by zero is not allowed.")
else:

    if a % b == 0:
        factor = a / b
        print(f"{a} is a multiple of {b} by a factor of {int(factor)}.")
    else:
        print(f"{a} is NOT a multiple of {b}.")