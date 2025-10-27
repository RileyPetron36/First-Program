user_input_number_str = input("Enter an integer: ")

number_to_check = int(user_input_number_str)

if number_to_check % 2 == 0:
        result_message = f"{number_to_check} is an even number."
else:
        result_message = f"{number_to_check} is an odd number."

print(result_message)