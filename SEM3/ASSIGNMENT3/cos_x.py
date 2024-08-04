import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def cos_x(x, n):
    cosine = 0.0
    sign = 1  
    for i in range(n):
        term = sign * (x**(2*i)) / factorial(2*i)
        cosine += term
        sign *= -1 

    return cosine
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n: "))
result = cos_x(x, n)
print("The cosine of " + str(x) + " using " + str(n) + " terms is: " + str(result))
