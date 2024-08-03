def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 48
num2 = 18

print("The GCD of", num1, "and", num2, "is:", gcd(num1, num2))
