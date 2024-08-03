import math

def is_krishnamurthy(number):
    digits = str(number)
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in digits)
    return sum_of_factorials == number


number = 145
if is_krishnamurthy(number):
    print(number, "is a Krishnamurthy number.")
else:
    print(number, "is not a Krishnamurthy number.")
