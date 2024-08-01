def is_perfect_number(num):
    if num <= 1:
        return False
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def is_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)
    sum_of_powers = sum(int(digit) ** power for digit in num_str)
    return sum_of_powers == num

number = int(input("Enter a number: "))

if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")

if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
