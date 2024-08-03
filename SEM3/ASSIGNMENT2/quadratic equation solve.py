import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return root1, root2

a = 1
b = -7
c = 10

roots = solve_quadratic(a, b, c)
print("The roots of the quadratic equation are:", roots)
