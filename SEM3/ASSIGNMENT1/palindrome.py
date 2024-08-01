def is_palindrome(n):
    original_number = n
    reversed_number = 0
    while n > 0:
        remainder = n % 10
        reversed_number = (reversed_number * 10) + remainder
        n = n // 10
    return original_number == reversed_number


number = int(input("Enter a number: "))

if is_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")
