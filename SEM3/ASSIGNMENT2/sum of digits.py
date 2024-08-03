def sum_of_digits(number):
    digits = str(number)
    sum_digits = sum(int(digit) for digit in digits)
    return sum_digits

number = 12345
result = sum_of_digits(number)
print("The sum of the digits of", number, "is:", result)
