def print_multiplication_table():
    
    try:
        num = int(input("Enter a number to print its multiplication table: "))
        print(f"Multiplication table for {num}:")
        for i in range(1, 11):
            product = num * i
            print(f"{num} x {i} = {product}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    print_multiplication_table()