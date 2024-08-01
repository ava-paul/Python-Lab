def reverse_number(n):
    reverse = 0
    while n > 0:
        remainder = n % 10
        reverse = (reverse * 10) + remainder
        n = n // 10
    return reverse
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("The reverse of the number is:", reversed_number)
