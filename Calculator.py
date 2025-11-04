num1 = float(input("Enter the first number: "))
operation = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))


if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':

    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."


print("Result:", result)