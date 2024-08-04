import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def sin_x(x, n):
    sine = 0.0
    sign = 1
    for i in range(n):
        term = sign * (x**(2*i + 1)) / factorial(2*i + 1)
        sine += term
        sign *= -1 
    return sine

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n: "))
result = sin_x(x, n)
print("The sine of " + str(x) + " using " + str(n) + " terms is: " + str(result))
