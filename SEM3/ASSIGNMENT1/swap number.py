def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num1, num2 = swap_numbers(num1, num2)
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)
