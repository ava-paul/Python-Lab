def print_multiplication_table(number):
    print("Multiplication table for", number, ":")
    for i in range(1, 11):  
        print(number, "x", i, "=", number * i)
try:
    user_input = int(input("Enter a number to display its multiplication table: "))
    print_multiplication_table(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
