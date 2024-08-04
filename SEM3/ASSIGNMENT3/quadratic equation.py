import math

def _solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 'No real roots'
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

solutions = _solve_quadratic_eqn(a, b, c)
if isinstance(solutions, str):
    print("Solution: " + solutions)
elif len(solutions) == 1:
    print("There is one real root: " + str(solutions[0]))
else:
    print("There are two real roots: " + str(solutions[0]) + " and " + str(solutions[1]))
